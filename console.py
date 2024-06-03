#!/usr/bin/python3
"""
The console v: 0.0.1
Contains the entry point of the command interpreter
"""

import cmd
import json
import re
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """
    Custom console class
    """

    prompt = '(hbnb) '
    storage = None

    def __init__(self, storage=None):
        super().__init__()
        self.storage = storage or models.storage  # Fallback to models.storage if not provided

    def do_quit(self, line):
        """
        Quit command.
        """
        return True

    def do_EOF(self, line):
        """
        EOF command.
        """
        return True

    def my_errors(self, line, num_of_args):
        """
        Displays error messages to the user.
        """
        classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]
        msg = ["** class name missing **",
               "** class doesn't exist **",
               "** instance id missing **",
               "** no instance found **",
               "** attribute name missing **",
               "** value missing **"]
        if not line:
            print(msg[0])
            return 1
        args = line.split()
        if num_of_args >= 1 and args[0] not in classes:
            print(msg[1])
            return 1
        elif num_of_args == 1:
            return 0
        if num_of_args >= 2 and len(args) < 2:
            print(msg[2])
            return 1
        d = self.storage.all()

        for i in range(len(args)):
            if args[i][0] == '"':
                args[i] = args[i].replace('"', "")
        key = args[0] + '.' + args[1]
        if num_of_args >= 2 and key not in d:
            print(msg[3])
            return 1
        elif num_of_args == 2:
            return 0
        if num_of_args >= 4 and len(args) < 3:
            print(msg[4])
            return 1
        if num_of_args >= 4 and len(args) < 4:
            print(msg[5])
            return 1
        return 0

    def handle_empty_line(self, line):
        """
        Eliminates empty lines.
        """
        return False

    def do_create(self, line):
        """
        Creates a new instance of a class.
        """
        if (self.my_errors(line, 1) == 1):
            return
        args = line.split(" ")
        try:
            cls = globals()[args[0]]
            obj = cls()
            obj.save()
            print(obj.id)
        except Exception as e:
            print("** class doesn't exist **")

    def do_show(self, line):
        """
        Prints a string representation of an instance.
        """
        if (self.my_errors(line, 2) == 1):
            return
        args = line.split()
        d = self.storage.all()
        if args[1][0] == '"':
            args[1] = args[1].replace('"', "")
        key = args[0] + '.' + args[1]
        print(d[key])

    def do_destroy(self, line):
        """
        Deletes an instance of a certain class.
        """
        if (self.my_errors(line, 2) == 1):
            return
        args = line.split()
        d = self.storage.all()
        if args[1][0] == '"':
            args[1] = args[1].replace('"', "")
        key = args[0] + '.' + args[1]
        del d[key]
        self.storage.save()

    def do_all(self, line):
        """
        Shows all instances, or instances of a certain class.
        """
        d = self.storage.all()
        if not line:
            print([str(x) for x in d.values()])
            return
        args = line.split()
        if (self.my_errors(line, 1) == 1):
            return
        print([str(v) for v in d.values() if v.__class__.__name__ == args[0]])

    def do_update(self, line):
        """
        Updates an instance based on the class name and id.
        """
        if (self.my_errors(line, 4) == 1):
            return
        args = line.split()
        d = self.storage.all()
        for i in range(len(args[1:]) + 1):
            if args[i][0] == '"':
                args[i] = args[i].replace('"', "")
        key = args[0] + '.' + args[1]
        attr_k = args[2]
        attr_v = args[3]
        try:
            if attr_v.isdigit():
                attr_v = int(attr_v)
            elif float(attr_v):
                attr_v = float(attr_v)
        except ValueError:
            pass
        class_attr = type(d[key]).__dict__
        if attr_k in class_attr.keys():
            try:
                attr_v = type(class_attr[attr_k])(attr_v)
            except Exception:
                print("Entered wrong value type")
                return
        setattr(d[key], attr_k, attr_v)
        self.storage.save()

    def my_count(self, class_n):
        """
        Method counts instances of a certain class.
        """
        count_instance = 0
        for instance_object in self.storage.all().values():
            if instance_object.__class__.__name__ == class_n:
                count_instance += 1
        print(count_instance)

    def default(self, line):
        """
        Method to take care of following commands.
        """
        names = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]
        commands = {
            "all": self.do_all,
            "count": self.my_count,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update
        }
        args = re.match(r"^(\w+)\.(\w+)\((.*)\)", line)
        if args:
            args = args.groups()
        if not args or len(args) < 2 or args[0] not in names or args[1] not in commands.keys():
            super().default(line)
            return
        if args[1] in ["all", "count"]:
            commands[args[1]](args[0])
        elif args[1] in ["show", "destroy"]:
            commands[args[1]](args[0] + ' ' + args[2])
        elif args[1] == "update":
            params = re.match(r"\"(.+?)\", (.+)", args[2])
            if params.groups()[1][0] == '{':
                dic_p = eval(params.groups()[1])
                for k, v in dic_p.items():
                    commands[args[1]](args[0] + " " + params.groups()[0] + " " + k + " " + str(v))
            else:
                rest = params.groups()[1].split(", ")
                commands[args[1]](args[0] + " " + params.groups()[0] + " " + rest[0] + " " + rest[1])

if __name__ == '__main__':
    cli = HBNBCommand(storage=models.storage)
    cli.cmdloop()
