{}
#!/usr/bin/python3
"""
Module file_storage serializes and deserializes JSON types
"""

import json
from models.base_model import BaseModel
from models.user import User

class FileStorage:
    """
    Custom class for file storage
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns dictionary representation of all objects
        """
        return self.__objects

    def new(self, obj):
        """Sets in __objects the object with the key <obj class name>.id"""
        self.__objects[obj.__class__.__name__ + '.' + str(obj.id)] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path)
        """
        with open(self.__file_path, 'w') as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects, if the JSON file exists,
        otherwise nothing happens
        """
        try:
            with open(self.__file_path, 'r') as f:
                data = json.load(f)
                for obj_data in data.values():
                    obj_class = obj_data.get("__class__")
                    if obj_class:
                        obj_instance = globals()[obj_class].load_from_dict(obj_data)
                        if obj_instance:
                            self.new(obj_instance)
        except FileNotFoundError:
            pass
        except Exception as e:
            print(f"Error reloading file storage: {e}")

# Assuming BaseModel has a staticmethod load_from_dict that creates an instance from a dictionary
# Example usage
if __name__ == "__main__":
    storage = FileStorage()
    # Add objects to storage and save them
    # storage.save()
    # Reload objects from storage
    # storage.reload()
