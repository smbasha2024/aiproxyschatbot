# Holidays
import uuid

from datetime import date, datetime, timezone

from sqlalchemy import (
    Column,
    String,
    UUID,
    Date,
    DateTime,
    Boolean,
    Text
)

from app.models.base_model import BaseModel


class Holidays(BaseModel):
    __tablename__ = "holidays"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    tenant_id = Column(
        String(255),
        nullable=False
    )

    holiday_date = Column(
        Date,
        nullable=False
    )

    holiday_name = Column(
        String(255),
        nullable=False
    )

    holiday_type = Column(
        String(50),
        nullable=False,
        default="PUBLIC"
    )

    description = Column(
        Text,
        nullable=True
    )

    is_optional = Column(
        Boolean,
        nullable=False,
        default=False
    )

    is_active = Column(
        Boolean,
        nullable=False,
        default=True
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