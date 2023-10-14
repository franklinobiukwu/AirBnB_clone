#!/usr/bin/python3
from models.user import User

# Create a User instance
user = User()
user.email = "test@example.com"
user.password = "my_password"
user.first_name = "John"
user.last_name = "Doe"

# Print attributes
print("User instance attributes:")
print(f"email: {user.email}")
print(f"password: {user.password}")
print(f"first_name: {user.first_name}")
print(f"last_name: {user.last_name}")

# Save and print the User instance
user.save()
print("User instance after save:")
print(user)

# Convert User instance to a dictionary and print
user_json = user.to_dict()
print("User instance as JSON:")
for key, value in user_json.items():
    print(f"\t{key}: ({type(value)}) - {value}")

# Create a new User instance from the JSON data
new_user = User(**user_json)
print("--")
print("New User instance created from JSON:")
print(new_user)

# Check if the original and new User instances are the same
print("--")
print("Are the original and new User instances the same?")
print(user is new_user)
