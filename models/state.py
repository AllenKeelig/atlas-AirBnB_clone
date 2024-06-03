#!/usr/bin/python3
# module for place.py

'''
defines state class which is a subclass of BaseModel.
Represents a state which can have cities in them

classes:
State: state in which location resides in

usage:
assist with the management of different models like users.
'''


class BaseModel:
    '''
    Base model class for all entities in the application
    '''
    def __init__(self, id: int):
        self.id = id

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.id}>"
