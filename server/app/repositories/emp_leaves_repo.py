
from app.schema.emp_leaves_dto import EmpLeaves as EmpLeavesDTO
from app.models.emp_leaves_model import EmpLeaves as EmpLeavesModel

from sqlalchemy import select, text
from typing import List


import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ---------------------- Repository (DB calls) ---------------------- #
class EmpLeavesRepo:
    """Handles all database interactions for authentication."""

    def __init__(self, db):
        self.db = db
    
    async def get_employee_leave_balance(self, tenant_id:str, emp_id:str, ) -> EmpLeavesDTO:
        print(f"Fetching Employee Leaves for Tenant: {tenant_id}, Employee ID: {emp_id}")

        stmt = select(EmpLeavesModel).where(
            EmpLeavesModel.employee_id == emp_id,
        )
        result = self.db.execute(stmt)
        existing = result.scalar_one_or_none()

        print(f"Existing Employee Leaves Record: {existing}")
        # Commit all changes after processing the list
        self.db.commit()

        print(f"SQLAlchemy DB INFO: {self.db}")

        if existing:
            return EmpLeavesDTO(
                tenant_id=existing.tenant_id or "",
                employee_id=existing.employee_id or "",
                employee_name=existing.employee_name or "",
                earned_leaves=existing.earned_leaves or 0,
                privileged_leaves=existing.privileged_leaves or 0,
                sick_leaves=existing.sick_leaves or 0,
                paternity_leaves=existing.paternity_leaves or 0,
                maternity_leaves=existing.maternity_leaves or 0,
                lop_count=existing.lop_count or 0,
            )

        # No record found
        return EmpLeavesDTO(
            tenant_id=tenant_id or "",
            employee_id=emp_id or "",
            employee_name="",
            earned_leaves=0,
            privileged_leaves=0,
            sick_leaves=0,
            paternity_leaves=0,
            maternity_leaves=0,
            lop_count=0,
        )
