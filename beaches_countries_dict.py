# beaches_countries_dict.py

# Dictionary of 8 beaches and the countries they are located in
beaches_countries_dict = {
                            "Bondi beach" : "Australia",
                            "Liku Beach" : "Fiji",
                            "Gunung Payung" : "Indonesia",
                            "White Beach" : "Philippines",
                            "Dhigurah Beach" : "Maldives",
                            "Perhentian Islands" : "Malaysia",
                            "Waikiki Beach" : "USA",
                            "Praslin Island" : "Seychelles"
                          }

# Print the entire dictionary
print("8 beaches and the countries they are located in: ")
print(beaches_countries_dict)

# Access and print the country of the 3rd beach
print()
print("Country of the 3rd beach: ")
print(beaches_countries_dict['Gunung Payung'])

# Update the country of the 6th beach
beaches_countries_dict['Perhentian Islands'] = 'Terengganu, Malaysia'
print()
print("Updated country of the 6th beach: ")
print(beaches_countries_dict)

# Delete the 5th beach from the dictionary
del beaches_countries_dict['Dhigurah Beach']
print()
print("Updated dictionary after deleting 5th beach: ")
print(beaches_countries_dict)

# Print the last key-value pair in the dictionary
print()
last_key = list(beaches_countries_dict.keys())[-1]
last_value = beaches_countries_dict[last_key]
print("The last key-value pair is: ")
print(last_key, ":" ,last_value)