# Holidays
from datetime import date
from typing import List

from sqlalchemy import select

from app.models.holidays_model import Holidays as HolidaysModel
from app.schema.holidays_dto import HolidayDTO


class HolidaysRepo:
    """Handles all database interactions for holidays."""

    def __init__(self, db):
        self.db = db

    async def get_holiday_calendar(
        self,
        tenant_id: str,
        year: int
    ) -> List[HolidayDTO]:

        start_date = date(year, 1, 1)
        end_date = date(year + 1, 1, 1)

        stmt = (
            select(HolidaysModel)
            .where(
                HolidaysModel.tenant_id == tenant_id,
                HolidaysModel.holiday_date >= start_date,
                HolidaysModel.holiday_date < end_date,
                HolidaysModel.is_active == True
            )
            .order_by(HolidaysModel.holiday_date)
        )

        result = self.db.execute(stmt)

        holidays = result.scalars().all()

        return [
            HolidayDTO(
                holiday_date=holiday.holiday_date,
                holiday_name=holiday.holiday_name,
                holiday_type=holiday.holiday_type,
                description=holiday.description,
                is_optional=holiday.is_optional
            )
            for holiday in holidays
        ]

    async def get_holidays(
        self,
        tenant_id: str,
        month: int,
        year: int
    ) -> List[HolidayDTO]:

        start_date = date(year, month, 1)

        if month == 12:
            end_date = date(year + 1, 1, 1)
        else:
            end_date = date(year, month + 1, 1)

        stmt = (
            select(HolidaysModel)
            .where(
                HolidaysModel.tenant_id == tenant_id,
                HolidaysModel.holiday_date >= start_date,
                HolidaysModel.holiday_date < end_date,
                HolidaysModel.is_active == True
            )
            .order_by(HolidaysModel.holiday_date)
        )

        result = self.db.execute(stmt)

        holidays = result.scalars().all()

        return [
            HolidayDTO(
                holiday_date=holiday.holiday_date,
                holiday_name=holiday.holiday_name,
                holiday_type=holiday.holiday_type,
                description=holiday.description,
                is_optional=holiday.is_optional
            )
            for holiday in holidays
        ]