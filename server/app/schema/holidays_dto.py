# Holidays
from datetime import date
from typing import Optional

from pydantic import BaseModel, Field

class HolidayDTO(BaseModel):
    holiday_date: date
    holiday_name: str
    holiday_type: str
    description: Optional[str] = None
    is_optional: bool = False
    is_active: bool = True

class HolidayCalendarRequest(BaseModel):
    tenant_id: str
    year: Optional[int] = Field(
        default=None,
        ge=2000,
        le=2100
    )
    month: Optional[int] = Field(
        default=None,
        ge=1,
        le=12
    )
    data: Optional[dict] = None