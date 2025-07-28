from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from ..database.core import Base 
import uuid

class FacilityGroup(Base):
    __tablename__ = 'facility_groups'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False, unique=True)

    def __repr__(self):
        return f"<FacilityGroup(id='{self.id}', name='{self.name}')>"
