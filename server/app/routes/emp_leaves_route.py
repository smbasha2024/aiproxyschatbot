from fastapi import APIRouter, HTTPException, Depends, Request, UploadFile, File, Form
from fastapi.responses import StreamingResponse

from app.configs.database import get_db

from app.services.emp_leaves_service import EmpLeavesService
from app.repositories.emp_leaves_repo import EmpLeavesRepo
from app.schema.emp_leaves_dto import EmpLeaveBalanceRequest
from app.schema.emp_leaves_dto import EmpLeaves as EmpLeavesDTO

from sqlalchemy.orm import Session
import logging
from typing import List


emp_leaves_route = APIRouter(prefix="/EmpLeaves", tags=["EmpLeaves"])
logger = logging.getLogger(__name__)

@emp_leaves_route.post("/GetEmployeeLeaveBalance", response_model=EmpLeavesDTO, response_model_exclude_none=True)
async def getEmployeeLeaveBalance(request: EmpLeaveBalanceRequest, db: Session = Depends(get_db)) -> EmpLeavesDTO:
    emp_leaves_service = EmpLeavesService(EmpLeavesRepo(db))
 
    print(
            f"Request Body Data: {request.data}, "
            f"Request Body Tenant: {request.tenant_id}, "
            f"Request Body Emp ID: {request.emp_id}"
        )

    emp_leaves = await emp_leaves_service.getEmployeeLeaveBalance(request.tenant_id, request.emp_id)

    #result = {
    #            "success": True,
    #            "status_code": 200,
    #            "message": "Data fetched successfully",
    #            "data": emp_leaves
    #        }

    print(f"Employe Leaves Results:  {emp_leaves}")

    return emp_leaves.model_dump(exclude_none=True)
