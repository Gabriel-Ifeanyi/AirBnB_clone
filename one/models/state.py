#!/usr/bin/python3
"""This module contains the State class"""

from models.base_model import BaseModel


class State(BaseModel):
    """This class defines State attributes"""

    name = ""  # empty string

    def __init__(self, *args, **kwargs):
        """This method initializes an instance of State"""
        super().__init__(*args, **kwargs)

