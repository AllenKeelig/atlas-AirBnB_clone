#!/usr/bin/python3
'''models base_models module'''

from uuid import uuid
from datetime import datetime


class BaseModel:
    '''A base model class providing common fields and behaviors
    for all models

    Attributes:
    id(str): a unique identifier for the model instance
    created_at (datetime): the timestamp when the model instance was created
    updated_at (datetime): the timestamp when the model was last updated
    '''


def __init__(self):
    '''Initializes a new instance of the BaseModel class.
    creates a unique identifier for the instance and set the creation
    and last update timestamp.
    '''


def save(self):
    '''Updates the updated_at timestamp to the current UTC time.
    this method stimulates the updating the record in a database.
    '''


def delete(self):
    '''Marks the model instance as deleted
    by setting the updated_at timestamp to None.
    This method simulates deleting the record from a database.
    '''
    self.updated_at = None


def __str__(self):
    """Returns a concise string representation of the model instance."""
    return "{}({}) - Created at: {}, Last updated at: {}".format(
        self.__class__.__name__, self.id, self.created_at, self.updated_at
    )
