#!/usr/bin/python3
'''
module for initialization
'''

from models.engine.file_storage import FileStorage

Storage = FileStorage()
Storage.reload()
