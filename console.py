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
    app_models = ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]
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
    def search_id(self, class_name, id):
        """Search if id is in json file with corresponding class"""
        file_path = FileStorage.get_file_path()
        # Load json file to dictionary variable
        with open(file_path, "r") as file:
            dict_var = json.load(file)
        print(dict_var)
        
    def del_instance(self, class_name, id):
        """Delete an instance with a given class name and id"""
        #TO BE IMPLEMENTED CORRECTLY
    
        file_path = FileStorage.get_file_path()
        
        # OPEN JSON FILE
        with open(file_path, "r+") as file:
            dict_var = json.load(file)
            
            if class_name in dict_var and id in dict_var[class_name]:
                del(dict_var[class_name][id])
            
                with open(file_path, "w") as file:
                    json.dump(dict_var, file)
                
                    return True
            else:
                return False

    def find_string_rep(self, class_name=None):
        #TO BE IMPLEMENETED CORRECTLY
        result_list = []
        if class_name is not None:
            # Print the string representation for the specified class
            return True
        else:
            # Print all the string representations from storage
            return False

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
            class_name = args
            model_class = self.model_classes[class_name]
            
            new_instance = model_class()
            new_instance.save()
            print(new_instance.id)
            

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
                    #Implement a functioning del_instance()
                    deleted = self.del_instance(class_name, id)
                    if not deleted:
                        print("** no instance found **")
    
    def do_all(self, args):
        """Prints all string representation of all instances based or not on the class name"""
        if args:
            class_name = args
            if class_name not in self.app_models:
                print("** class doesn't exist **")
            else:
                string_rep = []
                #Implement a functioning find_string_rep()
                string_rep = self.find_string_rep(class_name)
                print(string_rep)
        else: 
            string_rep = self.find_string_rep()
            print(string_rep)
            
    #EMPTYLINE 
    def emptyline(self):
        """Prevents emptyline from executing previous command"""
        pass

    #HELP METHODS
    def help_EOF(self):
        """Shows exit message for EOF"""
        print(f"Quit command to exit the program")

    def help_quit(self):
        """Shows exit message for Quit"""
        print(f"Quit command to exit the program")

    def help_create(self):
        """Handles the help default for create command"""
        print(f"Create instance of [class], saves to json, and print id")
    
    def help_show(self):
        """Handle the help default for show command"""
        print(f"Prints the string representation of an instance based on the class name and id")
    
    def help_destroy(self):
        """Handle the help default for the destroy command"""
        print(f"Deletes an instance based on the class name and id")

    def help_all(self):
        """Handle the help default for the all command"""
        print(f"Prints all string representation of all instances based or not on the class name.")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
