#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
from models.base_model import BaseModel
import models import storage


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter.

    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "
    my_list = {"BaseModel"}

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print("")
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_create(self, arg):
        """Create command to create a new instance of BaseModel."""
        if not arg:
            print("** class name missing **")
        elif arg not in models.my_list:
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Show command to print the string representation of an instance."""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in models.my_list:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + '.' + args[1]
            if key in models.storage.all():
                print(models.storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Destroy command to delete an instance."""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in models.my_list:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + '.' + args[1]
            if key in models.storage.all():
                del models.storage.all()[key]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """All command to print all instances."""
        args = arg.split()
        objs = []
        if not arg:
            for obj in models.storage.all().values():
                objs.append(str(obj))
            print(objs)
        elif args[0] not in models.my_list:
            print("** class doesn't exist **")
        else:
            for key, value in models.storage.all().items():
                if args[0] in key:
                    objs.append(str(value))
            print(objs)

    def do_update(self, arg):
        """Update command to update an instance."""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in models.my_list:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = args[0] + '.' + args[1]
            if key in models.storage.all():
                obj = models.storage.all()[key]
                setattr(obj, args[2], args[3])
                models.storage.save()
            else:
                print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
