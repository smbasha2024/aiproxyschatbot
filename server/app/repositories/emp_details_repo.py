from app.schema.emp_details_dto import EmpDetails as EmpDetailsDTO
from app.models.emp_details import EmpDetails as EmpDetailsModel

from sqlalchemy import select

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# ---------------------- Repository (DB calls) ---------------------- #
class EmpDetailsRepo:
    """Handles all database interactions for employee details."""

    def __init__(self, db):
        self.db = db

    async def get_employee_details(
        self,
        tenant_id: str,
        emp_id: str,
    ) -> EmpDetailsDTO:

        print(
            f"Fetching Employee Details for Tenant: "
            f"{tenant_id}, Employee ID: {emp_id}"
        )

        stmt = select(EmpDetailsModel).where(
            EmpDetailsModel.employee_id == emp_id,
        )

        result = self.db.execute(stmt)
        existing = result.scalar_one_or_none()

        print(f"Existing Employee Details Record: {existing}")

        if existing:
            return EmpDetailsDTO(
                employee_id=existing.employee_id or "",
                employee_name=existing.employee_name or "",
                email=existing.email or "",
                department_name=existing.department_name or "",
                role=existing.role or "",
                company_name=existing.company_name or "",
                joining_date=existing.joining_date,
                reporting_to=existing.reporting_to or "",
            )

        # No record found
        return EmpDetailsDTO(
            employee_id=emp_id or "",
            employee_name="",
            email="",
            department_name="",
            role="",
            company_name="",
            joining_date=None,
            reporting_to="",
        )