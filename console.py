#!/usr/bin/python3
"""Command interpreter for managing AirBnB objects"""

import cmd
import shlex
from models import storage

class AirbnbCmd(cmd.Cmd):
    """Command interpreter class"""

    prompt = '(AirBnB) '

    def emptyline(self):
        """Do nothing when empty line is entered"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_create(self, arg):
        """Create an object"""
        args = shlex.split(arg)
        if len(args) < 1:
            print("** class name missing **")
            return
        classname = args[0]
        try:
            class_ = getattr(models, classname)
        except AttributeError:
            print("** class doesn't exist **")
            return
        instance = class_()
        instance.save()
        print(instance.id)

    def do_show(self, arg):
        """Show an object"""
        args = shlex.split(arg)
        if len(args) < 2:
            print("** class name missing **")
            return
        classname = args[0]
        id = args[1]
        try:
            class_ = getattr(models, classname)
        except AttributeError:
            print("** class doesn't exist **")
            return
        objects = storage.all(class_)
        key = "{}.{}".format(classname, id)
        if key in objects:
            print(objects[key])
        else:
            print("** no instance found **")


if __name__ == '__main__':
    AirbnbCmd().cmdloop()
