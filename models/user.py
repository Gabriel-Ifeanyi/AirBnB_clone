#!/usr/bin/python3
"""User module"""

from models.base_model import BaseModel


class User(BaseModel):
    """This class defines User attributes"""

    email = "" # empty string
    password = "" # empty string
    first_name = "" # empty string
    last_name = "" # empty string

    def __init__(self, *args, **kwargs):
        """This method initializes an instance of User"""
        super().__init__(*args, **kwargs)
