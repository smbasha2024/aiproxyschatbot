# Leave applications
from datetime import date, datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, Field


# ============================================================
# APPLY LEAVE
# ============================================================

class ApplyLeaveRequest(BaseModel):
    tenant_id: str
    emp_id: str

    leave_type: str = Field(
        ...,
        description="EARNED, PRIVILEGED, SICK, PATERNITY, MATERNITY or LOP"
    )

    from_date: date
    to_date: date

    number_of_days: Decimal

    reason: Optional[str] = None

    data: Optional[dict] = None


# ============================================================
# CANCEL LEAVE
# ============================================================

class CancelLeaveRequest(BaseModel):
    tenant_id: str
    emp_id: str

    application_id: str

    data: Optional[dict] = None


# ============================================================
# APPROVE LEAVE
# ============================================================

class ApproveLeaveRequest(BaseModel):
    tenant_id: str

    approver_id: str

    application_id: str

    data: Optional[dict] = None


# ============================================================
# REJECT LEAVE
# ============================================================

class RejectLeaveRequest(BaseModel):
    tenant_id: str

    approver_id: str

    application_id: str

    rejection_reason: Optional[str] = None

    data: Optional[dict] = None


# ============================================================
# GET APPLICATION
# ============================================================

class GetLeaveApplicationRequest(BaseModel):
    tenant_id: str

    application_id: str

    data: Optional[dict] = None


# ============================================================
# GET EMPLOYEE APPLICATIONS
# ============================================================

class GetEmployeeLeaveApplicationsRequest(BaseModel):
    tenant_id: str
    emp_id: str

    data: Optional[dict] = None


# ============================================================
# GET PENDING APPROVALS
# ============================================================

class GetPendingLeaveApprovalsRequest(BaseModel):
    tenant_id: str
    approver_id: str

    data: Optional[dict] = None


# ============================================================
# RESPONSE DTO
# ============================================================

class LeaveAppln(BaseModel):
    application_id: str

    tenant_id: str

    employee_id: str
    employee_name: str = ""

    leave_type: str

    from_date: date
    to_date: date

    number_of_days: Decimal

    reason: Optional[str] = None

    status: str

    applied_date: datetime

    approved_by: Optional[str] = None
    approved_date: Optional[datetime] = None

    rejection_reason: Optional[str] = None