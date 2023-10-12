#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import json
"""Console module"""


class HBNBCommand(cmd.Cmd):

    """console class"""
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program
        """
        print
        return True

    def do_EOF(self, line):
        """break when EOF char is given
        """
        print
        return True

    def emptyline(self):
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and
prints the id
        """
        llst = line.split()
        if len(llst) < 1:
            print("** class name missing **")
        elif llst[0] == "BaseModel":
            b = BaseModel()
            print(b.id)
            b.save()
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Prints the string representation of an instance based on the class
name and id
        """
        llst = line.split()
        if len(llst) < 1:
            print("** class name missing **")
        elif llst[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(llst) < 2:
            print("** instance id missing **")
        else:
            try:
                b = BaseModel(storage.all()[f"{llst[0]}.{llst[1]}"])
                print(b)
            except KeyError:
                print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id (save the change
into the JSON file)
        """
        llst = line.split()
        if len(llst) < 1:
            print("** class name missing **")
        elif llst[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(llst) < 2:
            print("** instance id missing **")
        else:
            try:
                storage.remove(f"{llst[0]}.{llst[1]}")
            except KeyError:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
