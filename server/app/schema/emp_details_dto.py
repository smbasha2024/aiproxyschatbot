from datetime import date
from typing import Optional, Any

from pydantic import BaseModel


class EmpDetails(BaseModel):
    employee_id: Optional[str]= None
    employee_name: Optional[str]= None
    email: Optional[str]= None
    department_name: Optional[str]= None
    role: Optional[str]= None
    company_name: Optional[str]= None
    joining_date: Optional[date] = None
    reporting_to: Optional[str]= None

class EmpDetailsRequest(BaseModel):
    tenant_id: str
    emp_id: str
    data: Any