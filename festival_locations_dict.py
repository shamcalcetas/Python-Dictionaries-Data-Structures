# festival_locations_dict.py

# Dictionary of 8 festivals and their locations
festival_locations_dict = {
                            "Masskara" : "Bacolod",
                            "Dinagyang" : "Iloilo City",
                            "Songkran Festival" : "Thailand",
                            "Kadayawan Festival" : "Davao City",
                            "Giant Lantern Festival" : "City of Saint Fernando",
                            "Diwali" : "India",
                            "Obon Festival" : "Japan",
                            "Hermanus Whale Festival" : "South Africa"
                          }

# Print the entire dictionary
print("8 festivals and their locations: ")
print(festival_locations_dict)

# Access and print the location of the 4th festival
print()
print("Location of the 4th festival: ")
print(festival_locations_dict['Kadayawan Festival'])

# Update the location of the 6th festival
festival_locations_dict['Diwali'] = 'Southern India'
print()
print("Updated location of the 6th festival: ")
print(festival_locations_dict)

# Delete the 2nd festival from the dictionary
del festival_locations_dict['Dinagyang']
print()
print("Updated dictionary after deleting 2nd festival: ")
print(festival_locations_dict)

# Print the last key-value pair in the dictionary
print()
last_key = list(festival_locations_dict.keys())[-1]
last_value = festival_locations_dict[last_key]
print("The last key-value pair is: ")
print(last_key, ":" ,last_value)