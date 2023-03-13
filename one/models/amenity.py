#!/usr/bin/python3
"""This module contains the Amenity class"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """This class defines Amenity attributes"""

    name = ""  # empty string

    def __init__(self, *args, **kwargs):
        """This method initializes an instance of Amenity"""
        super().__init__(*args, **kwargs)

