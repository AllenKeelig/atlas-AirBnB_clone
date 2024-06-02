#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the metadata object
metadata = declarative_base()

# Define the BaseModel class with docstrings
class BaseModel:
    """
    A base class for SQLAlchemy models providing utility methods for CRUD operations.

    Attributes
    ----------
    _session : Session
        The SQLAlchemy session bound to this BaseModel.

    Methods
    -------
    save(obj)
        Commits the new object to the database.
    delete(obj)
        Deletes the object from the database.
    query()
        Queries the database for objects.
    reload(obj)
        Reloads the object from the database.
    count()
        Counts the number of objects in the database.
    all()
        Gets all objects from the database.
    get(id)
        Gets an object by its primary key.
    create_session()
        Creates a new session.
    close_session()
        Closes the current session.
    """

    # Initialize the session
    Session = sessionmaker(bind=create_engine('sqlite:///your_database.db'))

    # Class variables to hold the current database connection
    _session = None

    @classmethod
    def save(cls, obj):
        """
        Commit the new object to the database.

        Parameters
        ----------
        obj : object
            The object to commit to the database.
        """
        cls._session.add(obj)
        cls._session.commit()

    @classmethod
    def delete(cls, obj):
        """
        Delete the object from the database.

        Parameters
        ----------
        obj : object
            The object to delete from the database.
        """
        cls._session.delete(obj)
        cls._session.commit()

    @classmethod
    def query(cls):
        """
        Query the database for objects.

        Returns
        -------
        Query
            The SQLAlchemy query object.
        """
        return cls._session.query(cls)

    @classmethod
    def reload(cls, obj):
        """
        Reload the object from the database.

        Parameters
        ----------
        obj : object
            The object to reload from the database.

        Returns
        -------
        object
            The reloaded object.
        """
        return cls._session.query(cls).filter_by(id=obj.id).one()

    @classmethod
    def count(cls):
        """
        Count the number of objects in the database.

        Returns
        -------
        int
            The count of objects in the database.
        """
        return cls._session.query(cls).count()

    @classmethod
    def all(cls):
        """
        Get all objects from the database.

        Returns
        -------
        List[object]
            A list of all objects in the database.
        """
        return cls._session.query(cls).all()

    @classmethod
    def get(cls, id):
        """
        Get an object by its primary key.

        Parameters
        ----------
        id : int
            The primary key of the object to retrieve.

        Returns
        -------
        object
            The object with the given primary key.
        """
        return cls._session.query(cls).get(id)

    @classmethod
    def create_session(cls):
        """
        Create a new session.
        """
        cls._session = cls.Session()

    @classmethod
    def close_session(cls):
        """
        Close the current session.
        """
        cls._session.close()


class State(BaseModel):
    """Represent a state

    Attributes:
        name (str): The name of the state

    """
    name = ""
    def __init__(self, id: int):
        self.id = id

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.id}>"
