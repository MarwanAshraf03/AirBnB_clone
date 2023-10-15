#!/usr/bin/python3
"""Console module"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    """console class"""
    prompt = "(hbnb) "
    classes = {
        "BaseModel": BaseModel,
        "User": User
    }

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """break when EOF char is given
        """
        print()
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
        elif llst[0] in self.classes.keys():
            b = self.classes[llst[0]]()
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
        elif llst[0] not in self.classes.keys():
            print("** class doesn't exist **")
        elif len(llst) < 2:
            print("** instance id missing **")
        else:
            try:
                print(storage.all()[f"{llst[0]}.{llst[1]}"])
            except KeyError:
                print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id (save the change
into the JSON file)
        """
        llst = line.split()
        if len(llst) < 1:
            print("** class name missing **")
        elif llst[0] not in self.classes.keys():
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
            if llst[0] in self.classes.keys():
                for key in dictionary.keys():
                    if llst[0] in key:
                        plist.append(dictionary[key].__str__())
            else:
                print("** class doesn't exist **")
                return
        else:
            for key in dictionary.keys():
                plist.append(dictionary[key].__str__())
        print(plist)

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding
or updating attribute (save the change into the JSON file)
        """
        llst = line.split()
        if len(llst) < 1:
            print("** class name missing **")
            return
        elif llst[0] not in self.classes.keys():
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
        llst[3] = self.sset(llst[3])
        setattr(storage.all()[f"{llst[0]}.{llst[1]}"], llst[2], llst[3])
        storage.all()[f"{llst[0]}.{llst[1]}"].save()

    def sset(self, value):
        try:
            value = int(value)
        except ValueError:
            try:
                value = float(value)
            except ValueError:
                pass
        return value


if __name__ == '__main__':
    HBNBCommand().cmdloop()
