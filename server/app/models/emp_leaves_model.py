# app/models/reg_portal_evidences.py
import uuid
from datetime import datetime, timezone
from sqlalchemy import String, Column, UUID, DateTime, Numeric
from app.models.base_model import BaseModel

class EmpLeaves(BaseModel):
    __tablename__ = "emp_leaves"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tenant_id = Column(String(255), nullable=True)
    
    employee_id = Column(String(255), nullable=True)
    employee_name = Column(String(255), nullable=True)
    earned_leaves = Column(Numeric(10, 2), nullable=True)
    privileged_leaves = Column(Numeric(10, 2), nullable=True)
    sick_leaves = Column(Numeric(10, 2), nullable=True)
    paternity_leaves = Column(Numeric(10, 2), nullable=True)
    maternity_leaves = Column(Numeric(10, 2), nullable=True)
    lop_count = Column(Numeric(10, 2), nullable=True)

    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=datetime.now(timezone.utc))
    created_by = Column(String(255), nullable=True)
    updated_by = Column(String(255), nullable=True)