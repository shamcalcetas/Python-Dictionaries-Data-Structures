# technology_inventors_dict.py

# Dictionary of 6 technologies and their inventors
technology_inventors_dict = {
                              "Telephone" : "Alexander Graham Bell",
                              "Computer" : "Charles",
                              "Automobile" : "Karl Benz",
                              "Mobile Phone" : "Martin Cooper",
                              "Aeroplane " : "The Wright Brothers",
                              "Television" : "John Logie Baird"
                            }

# Print the entire dictionary
print("6 technologies and their inventors: ")
print(technology_inventors_dict)

# Access and print the inventor of the 4th technology
print()
print("Inventor of the 4th technology: ")
print(technology_inventors_dict['Mobile Phone'])

# Update the inventor of the 2nd technology
technology_inventors_dict['Computer'] = 'Charles Babbage'
print()
print("Updated inventor of the 2nd technology: ")
print(technology_inventors_dict)

# Delete the 6th technology from the dictionary
del technology_inventors_dict['Television']
print()
print("Updated dictionary after deleting 6th technology: ")
print(technology_inventors_dict)

# Print the last key-value pair in the dictionary
print()
last_key = list(technology_inventors_dict.keys())[-1]
last_value = technology_inventors_dict[last_key]
print("The last key-value pair is: ")
print(last_key, ":" ,last_value)