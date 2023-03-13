#!/usr/bin/python3
"""
This is the console for the AirBnB clone project
"""

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    The console class
    """
    prompt = "(hbnb) "

    def do_EOF(self, arg):
        """
        Exits console with EOF signal
        """
        return True

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def emptyline(self):
        """
        Does nothing when empty line is entered
        """
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it to the JSON file, and prints the id
        """
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the class name and id
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        try:
            obj_dict = storage.all()
            obj_key = "{}.{}".format(args[0], args[1])
            print(obj_dict[obj_key])
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id and saves the change into the JSON file
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        try:
            obj_dict = storage.all()
            obj_key = "{}.{}".format(args[0], args[1])
            del obj_dict[obj_key]
            storage.save()
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not on the class name
        """
        obj_dict = storage.all()
        obj_list = []
        for obj in obj_dict.values():
            if arg and obj.__class__.__name__ != arg:
                continue
            obj_list.append(str(obj))
        print(obj_list)

      def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or updating
        attribute (save the change into the JSON file). Usage: update <class
        name> <id> <attribute name> "<attribute value>"
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        elif args[1] not in ids:
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        obj = storage.all()[key]
        setattr(obj, args[2], args[3].replace('"', ''))
        storage.save()

    def emptyline(self):
        """
        Do nothing on empty line
        """
        pass

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        Exit program at end of file
        """
        print()
        return True

    def default(self, arg):
        """
        Default command when no other command is recognized. Method will check
        for <class name>.all() and <class name>.count() methods and execute
        them if found.
        """
        args = arg.split('.')
        if len(args) < 2:
            print("*** Unknown syntax: {}".format(arg))
            return
        if args[1] == 'all()':
            if args[0] in classes:
                self.do_all(args[0])
            else:
                print("** class doesn't exist **")
        elif args[1] == 'count()':
            if args[0] in classes:
                print(len(storage.all(cls=classes[args[0]])))
            else:
                print("** class doesn't exist **")
        else:
            print("*** Unknown syntax: {}".format(arg))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
