#!/usr/bin/python3
"""This module contains the Review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """This class defines Review attributes"""

    place_id = ""  # empty string
    user_id = ""  # empty string
    text = ""  # empty string

    def __init__(self, *args, **kwargs):
        """This method initializes an instance of Review"""
        super().__init__(*args, **kwargs)

