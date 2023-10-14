#!/usr/bin/python3
from models.user import User

user = User()
user.email = "test@example.com"
user.password = "my_password"
user.first_name = "John"
user.last_name = "Doe"
print("User instance:")
print(user)

user.save()
print("User instance after save:")
print(user)

user_json = user.to_dict()
print("User instance as JSON:")
for key, value in user_json.items():
    print(f"\t{key}: ({type(value)}) - {value}")
