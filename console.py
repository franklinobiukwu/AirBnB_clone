#!/usr/bin/python3
"""Implemntation of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""

    prompt = "(hbnb)"

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """EOF Command to handle Ctrl-D, to exit the program"""
        print()
        return True

    def emptyline(self):
        """Prevents emptyline from executing previous command"""
        pass

    def help_EOF(self):
        """Shows exit message for EOF"""
        return self.help_text()

    def help_quit(self):
        """Shows exit message for Quit"""
        return self.help_text()

    def help_text(self):
        """Help Text printed with program is exited"""
        print(f"Quit command to exit the program")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
