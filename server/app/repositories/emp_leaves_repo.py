
from app.schema.emp_leaves_dto import EmpLeaves as EmpLeavesDTO
from app.models.emp_leaves_model import EmpLeaves as EmpLeavesModel

from sqlalchemy import select
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
        stmt = select(EmpLeavesModel).where(
            EmpLeavesModel.employee_id == emp_id,
        )
        result = self.db.execute(stmt)
        existing = result.scalar_one_or_none()

        # Commit all changes after processing the list
        self.db.commit()

        emp_leaves = EmpLeavesDTO(
            #id="1",
            tenant_id=tenant_id,
            employee_id=emp_id,
            employee_name="S M Basha",
            earned_leaves=16,
            privileged_leaves=15,
            sick_leaves=8,
            paternity_leaves=5,
            maternity_leaves=0,
            lop_count=2,
        )

        return emp_leaves
