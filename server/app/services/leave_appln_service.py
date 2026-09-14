# Leave Applications
from typing import List, Optional

from app.repositories.leave_appln_repo import LeaveApplnRepo
from app.schema.leave_appln_dto import LeaveAppln as LeaveApplnDTO


class LeaveApplnService:

    def __init__(self, repo: LeaveApplnRepo):
        self.repo = repo

    # ============================================================
    # APPLY LEAVE
    # ============================================================

    async def apply_leave(
        self,
        tenant_id: str,
        emp_id: str,
        employee_name: str,
        leave_type: str,
        from_date,
        to_date,
        number_of_days,
        reason=None
    ) -> LeaveApplnDTO:

        if from_date > to_date:
            raise ValueError(
                "From date cannot be greater than to date."
            )

        allowed_leave_types = {
            "EARNED",
            "PRIVILEGED",
            "SICK",
            "PATERNITY",
            "MATERNITY",
            "LOP"
        }

        leave_type = leave_type.upper()

        if leave_type not in allowed_leave_types:
            raise ValueError(
                f"Invalid leave type: {leave_type}"
            )

        if number_of_days <= 0:
            raise ValueError(
                "Number of days must be greater than zero."
            )

        return await self.repo.apply_leave(
            tenant_id=tenant_id,
            emp_id=emp_id,
            employee_name=employee_name,
            leave_type=leave_type,
            from_date=from_date,
            to_date=to_date,
            number_of_days=number_of_days,
            reason=reason
        )

    # ============================================================
    # CANCEL LEAVE
    # ============================================================

    async def cancel_leave(
        self,
        tenant_id: str,
        emp_id: str,
        application_id: str
    ) -> LeaveApplnDTO:

        application = await self.repo.get_leave_application(
            tenant_id,
            application_id
        )

        if not application:
            raise ValueError(
                "Leave application not found."
            )

        if application.employee_id != emp_id:
            raise ValueError(
                "You are not authorized to cancel this leave."
            )

        if application.status not in {
            "PENDING",
            "APPROVED"
        }:
            raise ValueError(
                f"Leave cannot be cancelled when status is "
                f"{application.status}."
            )

        result = await self.repo.cancel_leave(
            tenant_id,
            emp_id,
            application_id
        )

        if not result:
            raise ValueError(
                "Unable to cancel leave application."
            )

        return result

    # ============================================================
    # APPROVE LEAVE
    # ============================================================

    async def approve_leave(
        self,
        tenant_id: str,
        approver_id: str,
        application_id: str
    ) -> LeaveApplnDTO:

        application = await self.repo.get_leave_application(
            tenant_id,
            application_id
        )

        if not application:
            raise ValueError(
                "Leave application not found."
            )

        if application.status != "PENDING":
            raise ValueError(
                f"Leave cannot be approved when status is "
                f"{application.status}."
            )

        result = await self.repo.approve_leave(
            tenant_id,
            approver_id,
            application_id
        )

        if not result:
            raise ValueError(
                "Unable to approve leave application."
            )

        return result

    # ============================================================
    # REJECT LEAVE
    # ============================================================

    async def reject_leave(
        self,
        tenant_id: str,
        approver_id: str,
        application_id: str,
        rejection_reason=None
    ) -> LeaveApplnDTO:

        application = await self.repo.get_leave_application(
            tenant_id,
            application_id
        )

        if not application:
            raise ValueError(
                "Leave application not found."
            )

        if application.status != "PENDING":
            raise ValueError(
                f"Leave cannot be rejected when status is "
                f"{application.status}."
            )

        result = await self.repo.reject_leave(
            tenant_id,
            approver_id,
            application_id,
            rejection_reason
        )

        if not result:
            raise ValueError(
                "Unable to reject leave application."
            )

        return result

    # ============================================================
    # GET APPLICATION
    # ============================================================

    async def get_leave_application(
        self,
        tenant_id: str,
        application_id: str
    ) -> LeaveApplnDTO:

        result = await self.repo.get_leave_application(
            tenant_id,
            application_id
        )

        if not result:
            raise ValueError(
                "Leave application not found."
            )

        return result

    # ============================================================
    # GET EMPLOYEE APPLICATIONS
    # ============================================================

    async def get_employee_leave_applications(
        self,
        tenant_id: str,
        emp_id: str
    ) -> List[LeaveApplnDTO]:

        return await self.repo.get_employee_leave_applications(
            tenant_id,
            emp_id
        )

    # ============================================================
    # GET PENDING APPROVALS
    # ============================================================

    async def get_pending_leave_approvals(
        self,
        tenant_id: str,
        approver_id: str
    ) -> List[LeaveApplnDTO]:

        return await self.repo.get_pending_leave_approvals(
            tenant_id,
            approver_id
        )