#!/usr/bin/python3
"""This module contains the City class"""

from models.base_model import BaseModel


class City(BaseModel):
    """This class defines City attributes"""

    state_id = ""  # empty string
    name = ""  # empty string

    def __init__(self, *args, **kwargs):
        """This method initializes an instance of City"""
        super().__init__(*args, **kwargs)
