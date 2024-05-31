#!/usr/bin/python3
'''command line interpreter'''

import cmd
from models import storage
from models import *
import sys
import re


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"
  

def do EOF(self, *args):
'''end of file command to exit program'''
