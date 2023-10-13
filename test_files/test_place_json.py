#!/usr/bin/python3
from models import storage
from models.place import Place

# Reload all objects from the storage
all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

# Create a new Place object
print("-- Create a new Place object --")
new_place = Place()
new_place.city_id = "city123"
new_place.user_id = "user456"
new_place.name = "Cozy Cottage"
new_place.description = "A charming cottage in the woods"
new_place.number_rooms = 2
new_place.number_bathrooms = 1
new_place.max_guest = 4
new_place.price_by_night = 100
new_place.latitude = 40.7128
new_place.longitude = -74.0060
new_place.amenity_ids = ["wifi", "parking", "fireplace"]

# Save the Place object
new_place.save()
print("--")
print("Place object after save:")
print(new_place)
