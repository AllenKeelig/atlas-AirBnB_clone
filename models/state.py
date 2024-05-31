#!/usr/bin/python3
#module for state.py

'''
defines state class which is a subclass of BaseModel.
which represents states that can contain multiple cities in the application.

classes:
state: a class that inherits from BaseModel.

usage:
this is part of a larger application and manages different models.
'''


class BaseModel:
    ''' Base model class for all entities in the application '''

    def __init__(self, id: int):
        self.id = id

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.id}>"
