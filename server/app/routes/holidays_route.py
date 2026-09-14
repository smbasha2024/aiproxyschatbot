# Holidays
from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.configs.database import get_db

from app.repositories.holidays_repo import HolidaysRepo
from app.services.holidays_service import HolidaysService

from app.schema.holidays_dto import (
    HolidayCalendarRequest,
    HolidayDTO
)

import logging
from typing import List


holidays_route = APIRouter(
    prefix="/Holidays",
    tags=["Holidays"]
)

logger = logging.getLogger(__name__)


@holidays_route.post(
    "/GetHolidayCalendar",
    response_model=List[HolidayDTO],
    response_model_exclude_none=True
)
async def getHolidayCalendar(
    request: HolidayCalendarRequest,
    db: Session = Depends(get_db)
) -> List[HolidayDTO]:

    holidays_service = HolidaysService(
        HolidaysRepo(db)
    )

    holidays = await holidays_service.get_holiday_calendar(
        request.tenant_id,
        request.year
    )

    print(
        f"Holiday Calendar Request: "
        f"Tenant={request.tenant_id}, "
        f"Year={request.year}"
    )

    print(f"Holiday Calendar Results: {holidays}")

    return [
        holiday.model_dump(exclude_none=True)
        for holiday in holidays
    ]


@holidays_route.post(
    "/GetHolidays",
    response_model=List[HolidayDTO],
    response_model_exclude_none=True
)
async def getHolidays(
    request: HolidayCalendarRequest,
    db: Session = Depends(get_db)
) -> List[HolidayDTO]:

    holidays_service = HolidaysService(
        HolidaysRepo(db)
    )

    holidays = await holidays_service.get_holidays(
        request.tenant_id,
        request.month,
        request.year
    )

    print(
        f"Holidays Request: "
        f"Tenant={request.tenant_id}, "
        f"Month={request.month}, "
        f"Year={request.year}"
    )

    print(f"Holidays Results: {holidays}")

    return [
        holiday.model_dump(exclude_none=True)
        for holiday in holidays
    ]