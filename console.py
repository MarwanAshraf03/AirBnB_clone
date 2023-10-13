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

    def do_all(self, line):
        """Prints all string representation of all instances based
or not on the class name
        """
        dictionary = storage.all()
        llst = line.split()
        plist = []
        if len(llst) > 0:
            if llst[0] == "BaseModel":
                for key in dictionary.keys():
                    if llst[0] in key:
                        plist.append(str(BaseModel(**dictionary[key])))
            else:
                print("** class doesn't exist **")
        else:
            for key in dictionary.keys():
                plist.append(str(BaseModel(**dictionary[key])))
        print(plist)

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding
or updating attribute (save the change into the JSON file)
        """
        llst = line.split()
        if len(llst) < 1:
            print("** class name missing **")
            return
        elif llst[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        elif len(llst) < 2:
            print("** instance id missing **")
            return
        else:
            try:
                storage.all()[f"{llst[0]}.{llst[1]}"]
            except KeyError:
                print("** no instance found **")
                return
        if len(llst) < 3:
            print("** attribute name missing **")
            return
        elif len(llst) < 4:
            print("** value missing **")
            return
        b = BaseModel(**storage.all()[f"{llst[0]}.{llst[1]}"])
        b.update(llst[2], llst[3])
        b.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
