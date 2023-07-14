#!/usr/bin/python3
"""entry point of the command interpreter"""

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Entry point of the command interpreter"""
    prompt = '(hbnb) '

    classes = ['BaseModel']

    def do_quit(self, arg):
        """Exit the program"""
        return True

    do_EOF = do_quit

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_create(self, arg):
        "Create an instance of BaseModel"
        if arg in self.classes:
            new = BaseModel()
            new.save()
            print(new.id)

        elif len(arg) < 1:
            print("** class name missing **")

        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        "Display an object given an existing id"
        objects = storage.all()
        args = arg.split(' ')
        key = ".".join(args)

        if len(args) >= 2 and args[0] in self.classes:
            try:
                print(objects[key])
            except KeyError:
                print("** no instance found **")

        elif len(args) == 0:
            print("** class name missing **")

        elif len(args) == 1 and args[0] in self.classes:
            print("** instance id missing **")

        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Destroy an object"""
        objects = storage.all()
        args = arg.split(' ')
        key = ".".join(args)

        if len(args) >= 2 and args[0] in self.classes:
            try:
                del objects[key]
                storage.save()
            except KeyError:
                print("** no instance found **")

        elif len(args) == 0:
            print("** class name missing **")

        elif len(args) == 1 and args[0] in self.classes:
            print("** instance id missing **")

        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Print string representation of an object
            based on class name or not
        """
        objects = storage.all()

        if len(arg) >= 1 and arg in self.classes:
            objList = [str(obj) for key, obj in objects.items() if arg in key]
            print(objList)

        elif len(arg) >= 1 and arg not in self.classes:
            print("** class doesn't exist **")

        else:
            objList = [str(obj) for key, obj in objects.items()]
            print(objList)

    def do_update(self, arg):
        """Updates an instance based on class name and id"""
        objects = storage.all()
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) >= 1 and args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) >= 2 and args[0] in self.classes:
            key = ".".join(args[0:2])
            if key not in objects.keys():
                print("** no instance found **")
            elif len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 3:
                print("** value missing **")
            else:
                obj = objects[key]
                attr = args[2]
                value = args[3].strip("'\"")
                setattr(obj, attr, value)
                obj.save()
                print(obj.id)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
