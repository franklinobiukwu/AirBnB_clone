#!/usr/bin/python3
from models import storage
from models.user import User

# Reload all objects from the storage
all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

# Create a new User object
print("-- Create a new User object --")
new_user = User()
new_user.email = "test@example.com"
new_user.password = "my_password"
new_user.first_name = "John"
new_user.last_name = "Doe"
new_user.save()

# Print the new User object
print("New User object:")
print(new_user)
