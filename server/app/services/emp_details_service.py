from app.repositories.emp_details_repo import EmpDetailsRepo
from app.schema.emp_details_dto import EmpDetails as EmpDetailsDTO

import logging

logger = logging.getLogger(__name__)


class EmpDetailsService:
    def __init__(self, repo: EmpDetailsRepo):
        self.repo = repo

    async def getEmployeeDetails(
        self,
        tenant_id: str,
        emp_id: str
    ) -> EmpDetailsDTO:

        emp_details = await self.repo.get_employee_details(
            tenant_id,
            emp_id
        )

        return emp_details