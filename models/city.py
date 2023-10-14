#!/usr/bin/python3
"""City class module"""
from models.base_model import BaseModel


class City(BaseModel):
    """Represents a single instance of a City"""

    state_id = ""
    name = ""
