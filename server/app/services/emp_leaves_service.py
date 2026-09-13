from app.configs.settings import settings
from app.repositories.emp_leaves_repo import EmpLeavesRepo
from app.schema.emp_leaves_dto import EmpLeaves as EmpLeavesDTO

from fastapi import HTTPException, UploadFile
import logging
from typing import List

logger = logging.getLogger(__name__)

class EmpLeavesService:
    def __init__(self, repo: EmpLeavesRepo):
        self.repo = repo
        
    async def getEmployeeLeaveBalance(self, tenant_id: str, emp_id: str) -> EmpLeavesDTO:
        emp_leaves = await self.repo.get_employee_leave_balance(tenant_id, emp_id)
        return emp_leaves
