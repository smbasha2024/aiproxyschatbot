from fastapi import APIRouter, Depends

from app.configs.database import get_db

from app.services.emp_details_service import EmpDetailsService
from app.repositories.emp_details_repo import EmpDetailsRepo
from app.schema.emp_details_dto import EmpDetailsRequest as EmpDetailsRequest
from app.schema.emp_details_dto import EmpDetails as EmpDetailsDTO

from sqlalchemy.orm import Session
import logging


emp_details_route = APIRouter(
    prefix="/EmpDetails",
    tags=["EmpDetails"]
)

logger = logging.getLogger(__name__)


@emp_details_route.post(
    "/GetEmployeeDetails",
    response_model=EmpDetailsDTO,
    response_model_exclude_none=True
)
async def getEmployeeDetails(
    request: EmpDetailsRequest,
    db: Session = Depends(get_db)
) -> EmpDetailsDTO:

    emp_details_service = EmpDetailsService(
        EmpDetailsRepo(db)
    )

    print(
        f"Request Body Data: {request.data}, "
        f"Request Body Tenant: {request.tenant_id}, "
        f"Request Body Emp ID: {request.emp_id}"
    )

    emp_details = await emp_details_service.getEmployeeDetails(
        request.tenant_id,
        request.emp_id
    )

    print(f"Employee Details Results: {emp_details}")

    return emp_details.model_dump(exclude_none=True)