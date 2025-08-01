from fastapi import HTTPException

class BookingError(HTTPException):
    """Base exception for booking-related errors"""
    pass

class BookingError(HTTPException):
    """Base exception for booking-related errors"""
    pass

class BookingNotFoundError(BookingError):
    def __init__(self, id=None):
        message = "Booking not found" if id is None else f"Booking with id {id} not found"
        super().__init__(status_code=404, detail=message)

class BookingCreationError(BookingError):
    def __init__(self, error: str):
        super().__init__(status_code=500, detail=f"Failed to create Booking: {error}")

class UserError(HTTPException):
    """Base exception for user-related errors"""
    pass

class UserNotFoundError(UserError):
    def __init__(self, user_id=None):
        message = "User not found" if user_id is None else f"User with id {user_id} not found"
        super().__init__(status_code=404, detail=message)

class PasswordMismatchError(UserError):
    def __init__(self):
        super().__init__(status_code=400, detail="New passwords do not match")

class InvalidPasswordError(UserError):
    def __init__(self):
        super().__init__(status_code=401, detail="Current password is incorrect")

class AuthenticationError(HTTPException):
    def __init__(self, message: str = "Could not validate user"):
        super().__init__(status_code=401, detail=message)

class FacilityNotFoundError(BookingError):
    def __init__(self, id=None):
        message = "Facility not found" if id is None else f"Facility with id {id} not found"
        super().__init__(status_code=404, detail=message)