## AirBnB clone - The console

This is a command-line interpreter that empowers users to input commands, including arguments when needed, to execute specific actions. Through this tool, users can create new objects, manipulate existing objects, access information about existing objects, and delete objects they have created.

This directory holds the source code files on the AirBnB clone project. This project falls under the course requirements for ALX SE program

# Concepts

	- Using the datetime module
	- Python packages and modules
	- Working with args & kwargs
	- Test-Driven Development (TDD) using the unittest module
	- Utilizing the cmd module
	- Employing the uuid module


# Prerequisites

This tool can be ran in the following Operating Systems:

    - Windows
    - Ubuntu
    - MacOS

The programming language to be installed so that the command-line interpreter can execute:

	Python 3.8.5 (or newer)

# Features

A command-line interpreter that enables users to perform some operations. The core features you will see in this project are:

    - Storing created objects in files
    - Modifying attributes of an object
    - Retrieving objects from files
    - Creating new objects (Users and Places)
    - Deleting an object
    - Interacting with retrieved objects
    - Enabling command autocompletion

# Execution Process

To initiate the command-line interpreter, you can launch it from any supported operating system's terminal. To begin an interactive session, simply execute the following command:

    ./console.py

Executing this command will open the command-line interface, presenting you with a prompt, indicating that the tool is ready to accept and process your commands indefinitely until you decide to conclude the session.

Alternatively, you can initiate the tool in a non-interactive mode by utilizing the subsequent command:

    echo "help" | ./console.py

Once the tool is running, you have the flexibility to carry out various operations directly from the command-line interface. By typing "help," you can view a comprehensive list of all available commands. Additionally, you can gather information on how to utilize any specific command from the list by using the following command structure:

    help <command_name>

# Example

Interactive Mode:

    $ ./console.py
    (hbnb) help

    Documented commands (type help <topic>):
    ========================================
    EOF  help  quit

    (hbnb) 
    (hbnb) 
    (hbnb) quit
    $

Non-interactive Mode:

    $ echo "help" | ./console.py
    (hbnb)

    Documented commands (type help <topic>):
    ========================================
    EOF  help  quit
    (hbnb) 
    $
    $ cat test_help
    help
    $
    $ cat test_help | ./console.py
    (hbnb)

    Documented commands (type help <topic>):
    ========================================
    EOF  help  quit
    (hbnb) 
    $/