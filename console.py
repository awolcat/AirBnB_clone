#!/usr/bin/python3
"""Entry point of the command interpreter"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.city import City
from models import storage


class HBNBCommand(cmd.Cmd):
    """Entry point of the command interpreter"""
    prompt = '(hbnb) '

    classes = ['BaseModel', 'User', 'Place',
               'State', 'Review', 'Amenity', 'City']

    def do_quit(self, arg):
        """Exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_create(self, arg):
        """Create an instance of BaseModel"""
        if arg in self.classes:
            new = eval(arg)()
            new.save()
            print(new.id)

        elif len(arg) < 1:
            print("** class name missing **")

        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Display an object given an existing id"""
        objects = storage.all()
        args = arg.split(' ')
        key = ".".join(args[1:])

        if len(args) >= 2 and args[0] in self.classes:
            try:
                print(objects[key])
            except KeyError:
                print("** no instance found **")

        elif len(args) >= 1 and len(args[0]) == 0:
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

        elif len(args) == 1 and len(args[0]) == 0:
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
            obj_list = [str(obj) for key, obj in objects.items() if arg in key]
            print(obj_list)

        elif len(arg) >= 1 and arg not in self.classes:
            print("** class doesn't exist **")

        else:
            obj_list = [str(obj) for key, obj in objects.items()]
            print(obj_list)

    def do_update(self, arg):
        """Updates an instance based on class name and id"""
        objects = storage.all()
        args = arg.split(' ')
        if len(args) >= 1 and len(args[0]) < 1:
            print("** class name missing **")
        elif len(args) >= 1 and args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1 and args[0] in self.classes:
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

    def default(self, arg):
        """Default command interpretation"""
        objects = storage.all()
        args = arg.split('.')
        if args[0] in self.classes and args[1] == 'all()':
            my_list = []
            for key, obj in objects.items():
                cls = key.split('.')[0]
                if args[0] == cls:
                    my_list.append(str(obj))
            print(my_list)

        elif args[0] in self.classes and args[1] == 'count()':
            count = 0
            for key, obj in objects.items():
                cls = key.split('.')[0]
                if args[0] == cls:
                    count = count + 1
            print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
