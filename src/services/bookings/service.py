from datetime import datetime, timedelta
from uuid import UUID
from sqlalchemy.orm import Session
from . import models
from src.services.auth.models import TokenData
from src.entities.booking import Booking
from src.entities.facility import Facility
from src.exceptions import BookingCreationError, BookingNotFoundError, FacilityNotFoundError
import logging

def create_booking(current_user: TokenData, db: Session, booking: models.BookingCreate) -> Booking:
    facility = db.query(Facility).filter(Facility.id == booking.facility_id).first()
    if not facility:
        logging.warning(f"Facility {booking.facility_id} not found")
        raise FacilityNotFoundError(booking.facility_id)

    try:
        new_booking = Booking(**booking.model_dump())
        new_booking.user_id = current_user.get_uuid()
        db.add(new_booking)
        db.commit()
        db.refresh(new_booking)
        logging.info(f"Created new booking for user: {current_user.get_uuid()}")
        return new_booking
    except Exception as e:
        logging.error(f"Failed to create booking for user {current_user.get_uuid()}. Error: {str(e)}")
        raise BookingCreationError(str(e))


def get_bookings_by_date(db: Session, booking_date_param: str) -> list[Booking]:
    booking_date = datetime.strptime(booking_date_param, "%Y-%m-%d").date()
    next_day = booking_date + timedelta(days=1)

    bookings = db.query(Booking).filter(Booking.event_date >= booking_date,Booking.event_date < next_day).all()
    if not bookings:
        return []
    return bookings


def get_booking_by_id(current_user: TokenData, db: Session, booking_id: UUID) -> Booking:
    booking = db.query(Booking).filter(Booking.id == booking_id).filter(Booking.user_id == current_user.get_uuid()).first()
    if not booking:
        logging.warning(f"Booking {booking_id} not found for user {current_user.get_uuid()}")
        raise BookingNotFoundError(booking_id)
    logging.info(f"Retrieved booking {booking_id} for user {current_user.get_uuid()}")
    return booking


def update_booking(current_user: TokenData, db: Session, booking_id: UUID, booking_update: models.BookingCreate) -> Booking:
    data = booking_update.model_dump(exclude_unset=True)
    db.query(Booking).filter(Booking.id == booking_id).filter(Booking.user_id == current_user.get_uuid()).update(data)
    db.commit()
    logging.info(f"Successfully updated booking {booking_id} for user {current_user.get_uuid()}")
    return get_booking_by_id(current_user, db, booking_id)


def delete_booking(current_user: TokenData, db: Session, booking_id: UUID) -> None:
    booking = get_booking_by_id(current_user, db, booking_id)
    db.delete(booking)
    db.commit()
    logging.info(f"Booking {booking_id} deleted by user {current_user.get_uuid()}")
