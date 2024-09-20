# technology_innovators_dict.py

# Dictionary of 8 technologies and their innovators
technology_innovators_dict = {
                                "Telephone" : "Alexander Graham Bell",
                                "Internet" : "Vinton Cerf",
                                "Computer" : " Charles Babbage",
                                "Automobile" : "Karl Benz",
                                "Mobile Phone" : "Martin Cooper",
                                "Aeroplane" : "The Wright Brothers",
                                "Television" : "John Logie Baird",
                                "Lightbulb" : "Thomas Edison"
                              }

# Print the entire dictionary
print("8 technologies and their innovators: ")
print(technology_innovators_dict)

# Access and print the innovator of the 4th technology
print()
print("Innovator of the 4th technology: ")
print(technology_innovators_dict['Automobile'])

# Update the innovator of the 2nd technology
technology_innovators_dict['Internet'] = 'Robert Kahn'
print()
print("Updated innovator of the 2nd technology: ")
print(technology_innovators_dict)

# Delete the 6th technology from the dictionary
del technology_innovators_dict['Aeroplane']
print()
print("Updated dictionary after deleting 6th technology: ")
print(technology_innovators_dict)

# Print the last key-value pair in the dictionary
print()
last_key = list(technology_innovators_dict.keys())[-1]
last_value = technology_innovators_dict[last_key]
print("The last key-value pair is: ")
print(last_key, ":" ,last_value)