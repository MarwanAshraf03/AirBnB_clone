#!/usr/bin/python3
import cmd
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
        """
        break when EOF char is given
        """
        print
        return True

    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
