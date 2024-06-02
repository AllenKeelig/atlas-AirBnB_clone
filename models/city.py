#!/usr/bin/python3
"""defines the city class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """represents a city

    Attributes:
        state_id (str): state id
        name (str): the name of the city
    """


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if "state_id" not in kwargs:
            self.state_id = ""
        if "name" not in kwargs:
            self.name = ""

# Example usage
if __name__ == "__main__":
    city = City(state_id="NY", name="New York")
    print(city.state_id)  # Should output: NY
    print(city.name)      # Should output: New York
