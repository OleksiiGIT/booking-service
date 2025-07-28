from fastapi import FastAPI
from .database.core import engine, Base
from .entities.user import User
from .entities.booking import Booking
from .entities.facility_group import FacilityGroup
from .entities.facility import Facility
from .entities.participant import Participant
from .api import register_routes
from .logging import configure_logging, LogLevels


configure_logging(LogLevels.info)

app = FastAPI()

""" Only uncomment below to create new tables, 
otherwise the tests will fail if not connected
"""
# Base.metadata.create_all(bind=engine)

register_routes(app)