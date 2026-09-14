# Leave Applications
from datetime import datetime, timezone
from typing import List, Optional
from uuid import UUID

from sqlalchemy import select

from app.models.leave_appln_model import LeaveAppln as LeaveApplnModel
from app.schema.leave_appln_dto import LeaveAppln as LeaveApplnDTO


class LeaveApplnRepo:

    def __init__(self, db):
        self.db = db

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
        reason: Optional[str] = None
    ) -> LeaveApplnDTO:

        leave_appln = LeaveApplnModel(
            tenant_id=tenant_id,
            employee_id=emp_id,
            employee_name=employee_name,
            leave_type=leave_type,
            from_date=from_date,
            to_date=to_date,
            number_of_days=number_of_days,
            reason=reason,
            status="PENDING",
            applied_date=datetime.now(timezone.utc),
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc),
            created_by=emp_id,
            updated_by=emp_id
        )

        self.db.add(leave_appln)
        self.db.commit()
        self.db.refresh(leave_appln)

        return self._to_dto(leave_appln)

    # ============================================================
    # CANCEL LEAVE
    # ============================================================

    async def cancel_leave(
        self,
        tenant_id: str,
        emp_id: str,
        application_id: str
    ) -> Optional[LeaveApplnDTO]:

        stmt = select(LeaveApplnModel).where(
            LeaveApplnModel.id == UUID(application_id),
            LeaveApplnModel.tenant_id == tenant_id,
            LeaveApplnModel.employee_id == emp_id
        )

        result = self.db.execute(stmt)
        leave_appln = result.scalar_one_or_none()

        if not leave_appln:
            return None

        leave_appln.status = "CANCELLED"
        leave_appln.updated_at = datetime.now(timezone.utc)
        leave_appln.updated_by = emp_id

        self.db.commit()
        self.db.refresh(leave_appln)

        return self._to_dto(leave_appln)

    # ============================================================
    # APPROVE LEAVE
    # ============================================================

    async def approve_leave(
        self,
        tenant_id: str,
        approver_id: str,
        application_id: str
    ) -> Optional[LeaveApplnDTO]:

        stmt = select(LeaveApplnModel).where(
            LeaveApplnModel.id == UUID(application_id),
            LeaveApplnModel.tenant_id == tenant_id
        )

        result = self.db.execute(stmt)
        leave_appln = result.scalar_one_or_none()

        if not leave_appln:
            return None

        leave_appln.status = "APPROVED"
        leave_appln.approved_by = approver_id
        leave_appln.approved_date = datetime.now(timezone.utc)
        leave_appln.updated_at = datetime.now(timezone.utc)
        leave_appln.updated_by = approver_id

        self.db.commit()
        self.db.refresh(leave_appln)

        return self._to_dto(leave_appln)

    # ============================================================
    # REJECT LEAVE
    # ============================================================

    async def reject_leave(
        self,
        tenant_id: str,
        approver_id: str,
        application_id: str,
        rejection_reason: Optional[str] = None
    ) -> Optional[LeaveApplnDTO]:

        stmt = select(LeaveApplnModel).where(
            LeaveApplnModel.id == UUID(application_id),
            LeaveApplnModel.tenant_id == tenant_id
        )

        result = self.db.execute(stmt)
        leave_appln = result.scalar_one_or_none()

        if not leave_appln:
            return None

        leave_appln.status = "REJECTED"
        leave_appln.approved_by = approver_id
        leave_appln.approved_date = datetime.now(timezone.utc)
        leave_appln.rejection_reason = rejection_reason
        leave_appln.updated_at = datetime.now(timezone.utc)
        leave_appln.updated_by = approver_id

        self.db.commit()
        self.db.refresh(leave_appln)

        return self._to_dto(leave_appln)

    # ============================================================
    # GET ONE APPLICATION
    # ============================================================

    async def get_leave_application(
        self,
        tenant_id: str,
        application_id: str
    ) -> Optional[LeaveApplnDTO]:

        stmt = select(LeaveApplnModel).where(
            LeaveApplnModel.id == UUID(application_id),
            LeaveApplnModel.tenant_id == tenant_id
        )

        result = self.db.execute(stmt)
        leave_appln = result.scalar_one_or_none()

        if not leave_appln:
            return None

        return self._to_dto(leave_appln)

    # ============================================================
    # GET EMPLOYEE APPLICATIONS
    # ============================================================

    async def get_employee_leave_applications(
        self,
        tenant_id: str,
        emp_id: str
    ) -> List[LeaveApplnDTO]:

        stmt = (
            select(LeaveApplnModel)
            .where(
                LeaveApplnModel.tenant_id == tenant_id,
                LeaveApplnModel.employee_id == emp_id
            )
            .order_by(LeaveApplnModel.applied_date.desc())
        )

        result = self.db.execute(stmt)
        applications = result.scalars().all()

        return [
            self._to_dto(application)
            for application in applications
        ]

    # ============================================================
    # GET PENDING APPROVALS
    # ============================================================

    async def get_pending_leave_approvals(
        self,
        tenant_id: str,
        approver_id: str
    ) -> List[LeaveApplnDTO]:

        # Initially this assumes approved_by is not yet assigned.
        # Manager/employee relationship validation can be added
        # through emp_details.manager_id.

        stmt = (
            select(LeaveApplnModel)
            .where(
                LeaveApplnModel.tenant_id == tenant_id,
                LeaveApplnModel.status == "PENDING"
            )
            .order_by(LeaveApplnModel.applied_date)
        )

        result = self.db.execute(stmt)
        applications = result.scalars().all()

        return [
            self._to_dto(application)
            for application in applications
        ]

    # ============================================================
    # DTO MAPPING
    # ============================================================

    def _to_dto(
        self,
        application: LeaveApplnModel
    ) -> LeaveApplnDTO:

        return LeaveApplnDTO(
            application_id=str(application.id),
            tenant_id=application.tenant_id,
            employee_id=application.employee_id,
            employee_name=application.employee_name or "",
            leave_type=application.leave_type,
            from_date=application.from_date,
            to_date=application.to_date,
            number_of_days=application.number_of_days,
            reason=application.reason,
            status=application.status,
            applied_date=application.applied_date,
            approved_by=application.approved_by,
            approved_date=application.approved_date,
            rejection_reason=application.rejection_reason
        )