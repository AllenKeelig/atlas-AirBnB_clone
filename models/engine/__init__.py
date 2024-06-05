#!/usr/bin/python3
'''
module for initialization
'''

from models.engine.file_storage import FileStorage

file_path = "models/engine/__init__.py"
Storage = FileStorage()
Storage.reload()
