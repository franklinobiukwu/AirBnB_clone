#!/usr/bin/python3
"""Implemntation of the command interpreter"""
import cmd
import json
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""

    prompt = "(hbnb) "
    app_models = ["BaseModel"]

    # HELPER METHODS#
    def search_id(self, class_name, id):
        """Search if id is in json file with corresponding class"""
        file_path = FileStorage.get_file_path()
        # Load json file to dictionary variable
        with open(file_path, "r") as file:
            dict_var = json.load(file)
        print(dict_var)

    # DO COMMANDS#
    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """EOF Command to handle Ctrl-D, to exit the program"""
        print()
        return True

    def do_create(self, args):
        """Creates new instance of BaseModel"""
        if len(args) == 0:
            print("** class name missing **")
        elif args not in self.app_models:
            print("** class doesn't exist **")
        else:
            new_base_model = BaseModel()
            new_base_model.save()
            print(new_base_model.id)

    def do_show(self, args):
        """Show string representation of an instance
        based on class name & id"""
        # Print *missing* if class name missing
        if not args:
            print("** class name missing **")
        else:
            try:
                class_name, id = args.split(" ")
            except (ValueError):
                return print("** instance id missing **")

            if class_name not in self.app_models:
                print("** class doesn't exist **")
            else:
                print("About to search id")
                self.search_id(class_name, id)
        # Print *no inst found* if id is not for class

    def emptyline(self):
        """Prevents emptyline from executing previous command"""
        pass

    def help_EOF(self):
        """Shows exit message for EOF"""
        print(f"Quit command to exit the program")

    def help_quit(self):
        """Shows exit message for Quit"""
        print(f"Quit command to exit the program")

    def help_create(self):
        """Handles the help default for create command"""
        print(f"Create instance of [class], saves to json, and print id")


if __name__ == '__main__':
    HBNBCommand().cmdloop()

