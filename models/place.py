#!/usr/bin/python3
"""This module contains the Place class"""

from models.base_model import BaseModel


class Place(BaseModel):
    """This class defines Place attributes"""

    city_id = ""  # empty string
    user_id = ""  # empty string
    name = ""  # empty string
    description = ""  # empty string
    number_rooms = 0  # integer 0
    number_bathrooms = 0  # integer 0
    max_guest = 0  # integer 0
    price_by_night = 0  # integer 0
    latitude = 0.0  # float 0.0
    longitude = 0.0  # float 0.0
    amenity_ids = []  # empty list

    def __init__(self, *args, **kwargs):
        """This method initializes an instance of Place"""
        super().__init__(*args, **kwargs)
