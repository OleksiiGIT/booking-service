from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from ..database.core import Base 
import uuid

class Participant(Base):
    __tablename__ = 'participants'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    booking_id = Column(UUID(as_uuid=True), ForeignKey('bookings.id'), nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return f"<Participant(id='{self.id}', booking_id='{self.booking_id}', user_id='{self.user_id}')>"
