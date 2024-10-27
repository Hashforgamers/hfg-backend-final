# models/__init__.py

from flask_sqlalchemy import SQLAlchemy

# Initialize the SQLAlchemy instance here
db = SQLAlchemy()

from .user import User  

from .amenity import Amenity  
from .availableGame import AvailableGame
from .businessRegistration import BusinessRegistration
from .contactInfo import ContactInfo
from .documentSubmitted import DocumentSubmitted
from .openingDay import OpeningDay
from .physicalAddress import PhysicalAddress
from .timing import Timing
from .vendor import Vendor 