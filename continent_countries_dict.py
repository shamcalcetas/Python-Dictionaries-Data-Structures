# continent_countries_dict.py

# Dictionary of 6 continents and a list of 3 countries for each
continent_countries_dict = {
                              "Asia" : "South Korea, Japan, Philippines",
                              "Africa" : "Ghana, Nigeria, Ethiopia",
                              "North America" : "Canada, Mexico, United States",
                              "South America" : "Chile, Brazil, Argentina",
                              "Europe" : "Germany, Italy, Greece",
                              "Oceania" : "Fiji, Australia, New Zealand",
                            }

# Print the entire dictionary
print("6 continents and a list of 3 countries for each: ")
print(continent_countries_dict)

# Access and print the countries of the 4th continent
print()
print("Countries of the 4th continent: ")
print(continent_countries_dict['South America'])

# Update the countries of the 5th continent
continent_countries_dict['Europe'] = 'France, Iceland, Switzerland'
print()
print("Updated countries of the 5th continent: ")
print(continent_countries_dict)

# Delete the 6th continent from the dictionary
del continent_countries_dict['Oceania']
print()
print("Updated dictionary after deleting 6th continent: ")
print(continent_countries_dict)

# Print the last key-value pair in the dictionary
print()
last_key = list(continent_countries_dict.keys())[-1]
last_value = continent_countries_dict[last_key]
print("The last key-value pair is: ")
print(last_key, ":" ,last_value)