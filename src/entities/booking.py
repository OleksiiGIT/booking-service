from sqlalchemy import Column, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime, timezone
from ..database.core import Base 

class Booking(Base):
    __tablename__ = 'bookings'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=False)
    facility_id = Column(UUID(as_uuid=True), ForeignKey('facilities.id'), nullable=False)
    event_date = Column(DateTime, nullable=True)
    created_at = Column(DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))

    def __repr__(self):
        return f"<Booking(id='{self.id}', user_id='{self.user_id}', facility_id='{self.facility_id}', event_date='{self.event_date}', created_at='{self.created_at}')>"
