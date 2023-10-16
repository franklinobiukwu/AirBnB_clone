#!/usr/bin/python3
"""Implemntation of the command interpreter"""
import cmd
import json
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage
from models.amenity import Amenity
from models.place import Place
from models.city import City
from models.review import Review
from models.user import User
from models.state import State


class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""

    prompt = "(hbnb) "
    app_models = ["BaseModel", "User", "Place", "State",
                  "City", "Amenity", "Review"]
    model_classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "Review": Review,
            "Place": Place,
            "City": City,
            "Amenity": Amenity,
        }

    # HELPER METHODS#

    def typecast_value(self, value):
        """Typecst value"""
        try:
            int_value = int(value)
            return int_value
        except ValueError:
            try:
                float_value = float(value)
                return float_value
            except ValueError:
                return value

    def search_id(self, class_name, id):
        """Search if id is in json file with corresponding class"""
        search_dict = {}
        file_path = FileStorage.get_file_path()

        with open(file_path, "r") as file:
            dict_var = json.load(file)

        if f"{class_name}.{id}" in dict_var:
            value = dict_var[f"{class_name}.{id}"]

            class_q = self.model_classes[class_name]
            return class_q(**value)
        else:
            return False

    def find_string_rep(self, class_name=None):
        """Prints all string representation of an instance"""

        result_list = []

        file_path = FileStorage.get_file_path()

        with open(file_path, "r") as file:
            dict_var = json.load(file)

        for key, value in dict_var.items():
            if class_name is not None:
                if key.split(".")[0] == class_name:
                    class_q = self.model_classes[class_name]
                    result_list.append(class_q(**value).juice())
            else:
                name_it = key.split(".")[0]
                class_q = self.model_classes[name_it]
                result_list.append(class_q(**value).juice())

        return result_list

    def del_instance(self, class_name, id):
        """Delete an instance with a given class name and id"""
        file_path = FileStorage.get_file_path()

        with open(file_path, "r") as file:
            dict_var = json.load(file)

        if f"{class_name}.{id}" in dict_var:
            del dict_var[f"{class_name}.{id}"]

            with open(file_path, "w") as file:
                json.dump(dict_var, file)

            return True
        else:
            return False

    def setting_attr(self, classname, id, attribute_name, value):
        """Searchs for Instance and sets the attribute"""

        file_path = FileStorage.get_file_path()

        value = self.typecast_value(value)

        with open(file_path, "r") as file:
            dict_var = json.load(file)

        instance_key = f"{classname}.{id}"

        if instance_key in dict_var:
            value_dict = dict_var[instance_key]

            value_dict[attribute_name] = value

            dict_var[instance_key] = value_dict

            with open(file_path, "w") as file:
                json.dump(dict_var, file)

            return True
        else:
            return False

    # DO METHODS
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
            class_name = args
            model_class = self.model_classes[class_name]

            new_instance = model_class()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, args):
        """Show string representation of an instance
        based on class name & id"""
        # Print *missing* if class name missing+9
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
                show_instance = self.search_id(class_name, id)
                if show_instance is False:
                    print("** no instance found **")
                else:
                    print(show_instance)

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        if not args:
            print("** class name missing **")
        else:
            split_args = args.split(" ")
            if len(split_args) == 1:
                class_name = split_args[0]
                if class_name not in self.app_models:
                    print("** class doesn't exist **")
                else:
                    print("** instance id missing **")
            elif len(split_args) == 2:
                class_name, id = split_args
                if class_name not in self.app_models:
                    print("** class doesn't exist **")
                else:
                    deleted = self.del_instance(class_name, id)
                    if not deleted:
                        print("** no instance found **")

    def do_all(self, args):
        """Prints all string representation of all
        instances based or not on the class name"""
        if args:
            class_name = args
            if class_name not in self.app_models:
                print("** class doesn't exist **")
            else:
                string_rep = self.find_string_rep(class_name)
                print(string_rep)
        else:
            string_rep = self.find_string_rep()
            print(string_rep)

    def do_update(self, args):
        """Updates an instance based on the class name
        and id by adding or updating attribute"""

        if len(args) == 0:
            print("** class name missing **")
            return

        update_args = args.split(" ")
        class_name = update_args[0]

        if class_name not in self.app_models:
            print("** class doesn't exist **")
            return

        if len(update_args) < 2:
            print("** instance id missing **")
            return

        instance_id = update_args[1]

        if len(update_args) < 3:
            print("** attribute name missing **")
            return

        attribute_name = update_args[2]

        if len(update_args) < 4:
            print("** value missing **")
            return

        value = update_args[3]

        instance = self.setting_attr(class_name, instance_id,
                                     attribute_name, value)

        if instance is False:
            print("** no instance found **")
            return

#   EMPTYLINE
    def emptyline(self):
        """Prevents emptyline from executing previous command"""
        pass

#   HELP METHODS
    def help_quit(self):
        """Quit command to exit the program"""
        print("Quit command to exit the program")

#   POSTCMD
    def postcmd(self, stop, line):
        """Executed every time user input is done executing"""
        if line == "quit":
            return True
        else:
            storage.reload()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
