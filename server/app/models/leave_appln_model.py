# Leave Applications
import uuid

from datetime import date, datetime, timezone

from sqlalchemy import (
    Column,
    String,
    UUID,
    Date,
    DateTime,
    Numeric,
    Text
)

from app.models.base_model import BaseModel


class LeaveAppln(BaseModel):
    __tablename__ = "leave_appln"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    tenant_id = Column(
        String(255),
        nullable=False
    )

    employee_id = Column(
        String(255),
        nullable=False
    )

    employee_name = Column(
        String(255),
        nullable=True
    )

    leave_type = Column(
        String(50),
        nullable=False
    )

    from_date = Column(
        Date,
        nullable=False
    )

    to_date = Column(
        Date,
        nullable=False
    )

    number_of_days = Column(
        Numeric(10, 2),
        nullable=False
    )

    reason = Column(
        Text,
        nullable=True
    )

    status = Column(
        String(50),
        nullable=False,
        default="PENDING"
    )

    applied_date = Column(
        DateTime,
        nullable=False,
        default=lambda: datetime.now(timezone.utc)
    )

    approved_by = Column(
        String(255),
        nullable=True
    )

    approved_date = Column(
        DateTime,
        nullable=True
    )

    rejection_reason = Column(
        Text,
        nullable=True
    )

    created_at = Column(
        DateTime,
        nullable=False,
        default=lambda: datetime.now(timezone.utc)
    )

    updated_at = Column(
        DateTime,
        nullable=False,
        default=lambda: datetime.now(timezone.utc)
    )

    created_by = Column(
        String(255),
        nullable=True
    )

    updated_by = Column(
        String(255),
        nullable=True
    )