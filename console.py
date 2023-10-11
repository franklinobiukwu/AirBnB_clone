#!/usr/bin/python3
"""Implemntation of the command interpreter"""
import cmd


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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
