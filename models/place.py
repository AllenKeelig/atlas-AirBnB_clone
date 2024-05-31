#!/usr/bin/python3
# module for place.py

  '''
    defines place class which is a subclass of BaseModel. Represents renting and listing.

    classes:
    place: name, description, information about the place such as number of rooms, location etc.

  usage:
      assist with the management of different models like users, states amenities, reviews places.
  '''

class BaseModel:
    '''
    Base model class for all entities in the application
    '''
    def __init__(self, id: int):
        self.id = id

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.id}>"

