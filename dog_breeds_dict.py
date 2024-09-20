# dog_breeds_dict.py

# Dictionary of 10 dog breeds and their sizes (small, medium, large)
car_specs_dict = {
                    "Golden Retriever" : "Large",
                    "Chihuahua" : "Small",
                    "Bulldog" : "Large",
                    "Labrador Retriever" : "Large",
                    "Cavalier King Charles" : "Medium",
                    "Pomeranian" : "Small",
                    "German Shepherd" : "Large",
                    "Alaskan Malamute" : "Large",
                    "Shiba Inu" : "Small",
                    "St. Bernard" : "Large"
                  }

# Print the entire dictionary
print("10 dog breeds and their sizes: ")
print(car_specs_dict)

# Access and print the size of the 5th breed
print()
print("Size of the 5th breed: ")
print(car_specs_dict['Cavalier King Charles'])

# Update the size of the 8th breed
car_specs_dict['Alaskan Malamute'] = 'Medium'
print()
print("Updated size of the 8th breed: ")
print(car_specs_dict)

# Delete the 6th breed from the dictionary
del car_specs_dict['Pomeranian']
print()
print("Updated dictionary after deleting 6th breed: ")
print(car_specs_dict)

# Print the last key-value pair in the dictionary
print()
last_key = list(car_specs_dict.keys())[-1]
last_value = car_specs_dict[last_key]
print("The last key-value pair is: ")
print(last_key, ":" ,last_value)