# Leave Applications
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.configs.database import get_db

from app.repositories.leave_appln_repo import LeaveApplnRepo
from app.services.leave_appln_service import LeaveApplnService

from app.schema.leave_appln_dto import (
    ApplyLeaveRequest,
    CancelLeaveRequest,
    ApproveLeaveRequest,
    RejectLeaveRequest,
    GetLeaveApplicationRequest,
    GetEmployeeLeaveApplicationsRequest,
    GetPendingLeaveApprovalsRequest,
    LeaveAppln as LeaveApplnDTO
)


leave_appln_route = APIRouter(
    prefix="/LeaveAppln",
    tags=["LeaveAppln"]
)


# ============================================================
# APPLY LEAVE
# ============================================================

@leave_appln_route.post(
    "/ApplyLeave",
    response_model=LeaveApplnDTO,
    response_model_exclude_none=True
)
async def apply_leave(
    request: ApplyLeaveRequest,
    db: Session = Depends(get_db)
) -> LeaveApplnDTO:

    service = LeaveApplnService(
        LeaveApplnRepo(db)
    )

    try:

        # Employee name can later be retrieved from EmpDetails.
        # For now this can be supplied/retrieved by the service.
        employee_name = ""

        result = await service.apply_leave(
            tenant_id=request.tenant_id,
            emp_id=request.emp_id,
            employee_name=employee_name,
            leave_type=request.leave_type,
            from_date=request.from_date,
            to_date=request.to_date,
            number_of_days=request.number_of_days,
            reason=request.reason
        )

        return result

    except ValueError as ex:

        raise HTTPException(
            status_code=400,
            detail=str(ex)
        )


# ============================================================
# CANCEL LEAVE
# ============================================================

@leave_appln_route.post(
    "/CancelLeave",
    response_model=LeaveApplnDTO,
    response_model_exclude_none=True
)
async def cancel_leave(
    request: CancelLeaveRequest,
    db: Session = Depends(get_db)
) -> LeaveApplnDTO:

    service = LeaveApplnService(
        LeaveApplnRepo(db)
    )

    try:

        result = await service.cancel_leave(
            tenant_id=request.tenant_id,
            emp_id=request.emp_id,
            application_id=request.application_id
        )

        return result

    except ValueError as ex:

        raise HTTPException(
            status_code=400,
            detail=str(ex)
        )


# ============================================================
# APPROVE LEAVE
# ============================================================

@leave_appln_route.post(
    "/ApproveLeave",
    response_model=LeaveApplnDTO,
    response_model_exclude_none=True
)
async def approve_leave(
    request: ApproveLeaveRequest,
    db: Session = Depends(get_db)
) -> LeaveApplnDTO:

    service = LeaveApplnService(
        LeaveApplnRepo(db)
    )

    try:

        result = await service.approve_leave(
            tenant_id=request.tenant_id,
            approver_id=request.approver_id,
            application_id=request.application_id
        )

        return result

    except ValueError as ex:

        raise HTTPException(
            status_code=400,
            detail=str(ex)
        )


# ============================================================
# REJECT LEAVE
# ============================================================

@leave_appln_route.post(
    "/RejectLeave",
    response_model=LeaveApplnDTO,
    response_model_exclude_none=True
)
async def reject_leave(
    request: RejectLeaveRequest,
    db: Session = Depends(get_db)
) -> LeaveApplnDTO:

    service = LeaveApplnService(
        LeaveApplnRepo(db)
    )

    try:

        result = await service.reject_leave(
            tenant_id=request.tenant_id,
            approver_id=request.approver_id,
            application_id=request.application_id,
            rejection_reason=request.rejection_reason
        )

        return result

    except ValueError as ex:

        raise HTTPException(
            status_code=400,
            detail=str(ex)
        )


# ============================================================
# GET ONE APPLICATION
# ============================================================

@leave_appln_route.post(
    "/GetLeaveApplication",
    response_model=LeaveApplnDTO,
    response_model_exclude_none=True
)
async def get_leave_application(
    request: GetLeaveApplicationRequest,
    db: Session = Depends(get_db)
) -> LeaveApplnDTO:

    service = LeaveApplnService(
        LeaveApplnRepo(db)
    )

    try:

        result = await service.get_leave_application(
            tenant_id=request.tenant_id,
            application_id=request.application_id
        )

        return result

    except ValueError as ex:

        raise HTTPException(
            status_code=404,
            detail=str(ex)
        )


# ============================================================
# GET EMPLOYEE LEAVE APPLICATIONS
# ============================================================

@leave_appln_route.post(
    "/GetEmployeeLeaveApplications",
    response_model=List[LeaveApplnDTO],
    response_model_exclude_none=True
)
async def get_employee_leave_applications(
    request: GetEmployeeLeaveApplicationsRequest,
    db: Session = Depends(get_db)
) -> List[LeaveApplnDTO]:

    service = LeaveApplnService(
        LeaveApplnRepo(db)
    )

    return await service.get_employee_leave_applications(
        tenant_id=request.tenant_id,
        emp_id=request.emp_id
    )


# ============================================================
# GET PENDING LEAVE APPROVALS
# ============================================================

@leave_appln_route.post(
    "/GetPendingLeaveApprovals",
    response_model=List[LeaveApplnDTO],
    response_model_exclude_none=True
)
async def get_pending_leave_approvals(
    request: GetPendingLeaveApprovalsRequest,
    db: Session = Depends(get_db)
) -> List[LeaveApplnDTO]:

    service = LeaveApplnService(
        LeaveApplnRepo(db)
    )

    return await service.get_pending_leave_approvals(
        tenant_id=request.tenant_id,
        approver_id=request.approver_id
    )