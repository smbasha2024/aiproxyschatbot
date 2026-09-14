# Holidays

from datetime import date
from typing import List

from app.repositories.holidays_repo import HolidaysRepo
from app.schema.holidays_dto import HolidayDTO


class HolidaysService:

    def __init__(self, repo: HolidaysRepo):
        self.repo = repo

    async def get_holiday_calendar(
        self,
        tenant_id: str,
        year: int | None = None
    ) -> List[HolidayDTO]:

        if year is None:
            year = date.today().year

        holidays = await self.repo.get_holiday_calendar(
            tenant_id,
            year
        )

        return holidays

    async def get_holidays(
        self,
        tenant_id: str,
        month: int,
        year: int | None = None
    ) -> List[HolidayDTO]:

        if year is None:
            year = date.today().year

        holidays = await self.repo.get_holidays(
            tenant_id,
            month,
            year
        )

        return holidays