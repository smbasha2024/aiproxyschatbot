# app/dto/emp_leaves_dto.py
from pydantic import BaseModel
from datetime import datetime
from typing import Any, Optional

class EmpLeaves(BaseModel):
    id: Optional[str]= None
    tenant_id: Optional[str]= None

    employee_id: Optional[str]= None
    employee_name: Optional[str]= None
    earned_leaves: Optional[float]= None
    privileged_leaves: Optional[float]= None
    sick_leaves: Optional[float]= None
    paternity_leaves: Optional[float]= None
    maternity_leaves: Optional[float]= None
    lop_count: Optional[float]= None

    created_at: Optional[datetime]= None
    updated_at: Optional[datetime]= None
    created_by: Optional[str]= None
    updated_by: Optional[str]= None

class EmpLeaveBalanceRequest(BaseModel):
    tenant_id: str
    emp_id: str
    data: Any