from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, ConfigDict

class BookingBase(BaseModel):
    facility_id: UUID
    event_date: datetime

class BookingCreate(BookingBase):
    pass

class BookingResponse(BookingBase):
    id: UUID
    user_id: UUID
    
    model_config = ConfigDict(from_attributes=True)
