# space_missions_dict.py

# Dictionary of 5 space missions and their corresponding years
space_missions_dict = {
                        "Apollo 11" : "1969",
                        "Artemis I" : "2022",
                        "Apollo 13" : "1970",
                        "Expedition 2" : " 2001",
                        "Lunar Orbiter 1" : "1966"
                      }

# Print the entire dictionary
print("5 space missions and their corresponding years: ")
print(space_missions_dict)

# Access and print the year of the 3rd mission
print()
print("Year of the 3rd mission: ")
print(space_missions_dict['Apollo 13'])

# Update the year of the 2nd mission
space_missions_dict['Artemis I'] = '2021'
print()
print("Updated year of the 2nd mission: ")
print(space_missions_dict)

# Delete the 4th mission from the dictionary
del space_missions_dict['Expedition 2']
print()
print("Updated dictionary after deleting 4th mission: ")
print(space_missions_dict)

# Print the last key-value pair in the dictionary
print()
last_key = list(space_missions_dict.keys())[-1]
last_value = space_missions_dict[last_key]
print("The last key-value pair is: ")
print(last_key, ":" ,last_value)