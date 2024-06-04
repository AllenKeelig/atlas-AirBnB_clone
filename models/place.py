#!/usr/bin/python3
from models.base_model import BaseModel

class State(BaseModel):
    '''
    Represents a state in the application.
    '''

    def __init__(self, *args, name=None, **kwargs):
        '''
        Initializes a State instance.

        Parameters:
        - name (str): The name of the state.
        - *args, **kwargs: Additional arguments to pass to the parent class constructor.
        '''
        super().__init__(*args, **kwargs)
        self.name = name

    def __repr__(self):
        '''
        Returns a string representation of the State instance.
        '''
        return f"<{self.__class__.__name__} {self.id} - {self.name}>"
