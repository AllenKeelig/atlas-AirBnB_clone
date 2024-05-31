#!/usr/bin/python3

import sys

class User:
    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password


    def greet(self, custom_message=None):
        '''git
        generate a greeting message for the user.
        
        Parameters:
        - custom_message (str): an optional custom message to append to the greeting.
        
        Returns:
        - str: a personalized greeting message.
        '''
        full_name = f"{self.first_name} {self.last_name}"
        if custom_message:
            return f"{custom_message}, {full_name}"
        else:
            return f"Hello, {full_name}!"
        
        
    def create_user(first_name, last_name, email, password):
        '''
        create a new user profile.

        parameters:
        - first_name (str): the user's first name.
        - last_name (str): the user's last name.
        - email (str): the user's email address.
        - password (str): the user's password.

        Returns:
        - User: a new user object represting the created profile.
        '''
        return User(first_name, last_name, email, password)
    
    
    def display_users(users):
        '''
        display information about the given user.

        parameters:
        - users (list of user objects): a list of user objects to display information
        '''
        for user in users:
            print(f"Name: {user.fist_name} {user.last_name}")
            print(f"Email: {user.email}")
            print(user.greet())
