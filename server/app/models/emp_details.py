from datetime import date
import uuid

from sqlalchemy import String, Column, UUID, Date, DateTime
from app.models.base_model import BaseModel


class EmpDetails(BaseModel):
    __tablename__ = "emp_details"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    employee_id = Column(String(255), nullable=True)
    employee_name = Column(String(255), nullable=True)
    email = Column(String(255), nullable=True)
    department_name = Column(String(255), nullable=True)
    role = Column(String(255), nullable=True)
    company_name = Column(String(255), nullable=True)
    joining_date = Column(Date, nullable=True)
    reporting_to = Column(String(255), nullable=True)
    manager_id = Column(String(255), nullable=True)

    created_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, nullable=True)
    created_by = Column(String(255), nullable=True)
    updated_by = Column(String(255), nullable=True)