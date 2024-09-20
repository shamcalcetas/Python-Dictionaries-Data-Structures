# planet_distances_dict.py

# Dictionary of 8 planets and their distances from the sun (in million kilometers)
planet_distances_dict = {
                          "Mercury" : "57,900,000 km",
                          "Venus" : "108,200,000 km",
                          "Earth" : "149,600,000 km",
                          "Mars" : "227,900,000 km",
                          "Jupiter" : "778,600,000 km",
                          "Saturn" : "1,433,500,000 km",
                          "Uranus" : "2,872,500,000 km",
                          "Neptune" : "4,495,100,000 km"
                        }

# Print the entire dictionary
print("8 planets and their distances from the sun: ")
print(planet_distances_dict)

# Access and print the distance of the 3rd planet
print()
print("Distance of the 3rd planet: ")
print(planet_distances_dict['Earth'])

# Update the distance of the 5th planet
planet_distances_dict['Jupiter'] = '778,000,000'
print()
print("Updated distance of the 5th planet: ")
print(planet_distances_dict)

# Delete the 7th planet from the dictionary
del planet_distances_dict['Uranus']
print()
print("Updated dictionary after deleting 7th planet: ")
print(planet_distances_dict)

# Print the last key-value pair in the dictionary
print()
last_key = list(planet_distances_dict.keys())[-1]
last_value = planet_distances_dict[last_key]
print("The last key-value pair is: ")
print(last_key, ":" ,last_value)