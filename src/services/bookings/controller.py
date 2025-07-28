from fastapi import APIRouter, status
from typing import List
from uuid import UUID

from ...database.core import DbSession
from . import  models
from . import service
from ..auth.service import CurrentUser

router = APIRouter(
    prefix="/bookings",
    tags=["Bookings"]
)

@router.post("/", response_model=models.BookingResponse, status_code=status.HTTP_201_CREATED)
def create_booking(db: DbSession, booking: models.BookingCreate, current_user: CurrentUser):
    return service.create_booking(current_user, db, booking)


@router.get("/{booking_date}", response_model=List[models.BookingResponse])
def get_bookings_by_date(db: DbSession, booking_date: str):
    return service.get_bookings_by_date(db, booking_date)


@router.get("/{booking_id}", response_model=models.BookingResponse)
def get_booking(db: DbSession, booking_id: UUID, current_user: CurrentUser):
    return service.get_booking_by_id(current_user, db, booking_id)


@router.put("/{booking_id}", response_model=models.BookingResponse)
def update_booking(db: DbSession, booking_id: UUID, booking_update: models.BookingCreate, current_user: CurrentUser):
    return service.update_booking(current_user, db, booking_id, booking_update)


@router.delete("/{booking_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_booking(db: DbSession, booking_id: UUID, current_user: CurrentUser):
    service.delete_booking(current_user, db, booking_id)
