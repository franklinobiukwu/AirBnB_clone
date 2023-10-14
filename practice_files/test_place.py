
#!/usr/bin/python3
from models.place import Place

# Create a Place instance
place = Place()
place.city_id = "city123"
place.user_id = "user456"
place.name = "Cozy Cottage"
place.description = "A charming cottage in the woods"
place.number_rooms = 2
place.number_bathrooms = 1
place.max_guest = 4
place.price_by_night = 100
place.latitude = 40.7128
place.longitude = -74.0060
place.amenity_ids = ["wifi", "parking", "fireplace"]

# Print attributes of the Place instance
print("Place instance attributes:")
print(f"city_id: {place.city_id}")
print(f"user_id: {place.user_id}")
print(f"name: {place.name}")
print(f"description: {place.description}")
print(f"number_rooms: {place.number_rooms}")
print(f"number_bathrooms: {place.number_bathrooms}")
print(f"max_guest: {place.max_guest}")
print(f"price_by_night: {place.price_by_night}")
print(f"latitude: {place.latitude}")
print(f"longitude: {place.longitude}")
print(f"amenity_ids: {place.amenity_ids}")

# Save the Place instance
place.save()
print("--")
print("Place instance after save:")
print(place)

# Convert Place instance to a dictionary and print
place_json = place.to_dict()
print("--")
print("Place instance as JSON:")
for key, value in place_json.items():
    print(f"\t{key}: ({type(value)}) - {value}")

# Create a new Place instance from the JSON data
new_place = Place(**place_json)
print("--")
print("New Place instance created from JSON:")
print(new_place)

# Check if the original and new Place instances are the same
print("--")
print("Are the original and new Place instances the same?")
print(place is new_place)


print("NEW TEST FOR DICT")


# Create a Place instance
place = Place()
place.city_id = "city123"
place.user_id = "user456"
place.name = "Cozy Cottage"
place.description = "A charming cottage in the woods"
place.number_rooms = 2
place.number_bathrooms = 1
place.max_guest = 4
place.price_by_night = 100
place.latitude = 40.7128
place.longitude = -74.0060
place.amenity_ids = ["wifi", "parking", "fireplace"]

# Print attributes of the Place instance
print("Place instance attributes:")
print(f"city_id: {place.city_id}")
print(f"user_id: {place.user_id}")
print(f"name: {place.name}")
print(f"description: {place.description}")
print(f"number_rooms: {place.number_rooms}")
print(f"number_bathrooms: {place.number_bathrooms}")
print(f"max_guest: {place.max_guest}")
print(f"price_by_night: {place.price_by_night}")
print(f"latitude: {place.latitude}")
print(f"longitude: {place.longitude}")
print(f"amenity_ids: {place.amenity_ids}")

# Save the Place instance
place.save()
print("--")
print("Place instance after save:")
print(place)

# Convert Place instance to a dictionary and print
place_json = place.to_dict()
print("--")
print("Place instance as JSON:")
for key, value in place_json.items():
    print(f"\t{key}: ({type(value)}) - {value}")

# Create a new Place instance from the JSON data
new_place = Place(**place_json)
print("--")
print("New Place instance created from JSON:")
print(new_place)

# Check if the original and new Place instances are the same
print("--")
print("Are the original and new Place instances the same?")
print(place is new_place)
