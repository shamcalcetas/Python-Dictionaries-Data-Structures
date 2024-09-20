# country_capital_dict.py

# Dictionary of 12 countries and their capitals
country_capital_dict = {
                          "Japan" : "Tokyo",
                          "South Korea" : "Seoul",
                          "China" : "Beijing",
                          "Philippines" : "Manila",
                          "Thailand" : "Bangkok",
                          "Singapore" : "Singapore",
                          "Indonesia" : "Jakarta",
                          "Iceland" : "Reykjavik",
                          "Denmark" : "Copenhagen",
                          "Spain ": "Madrid",
                          "United States of America" : "Washington, D.C",
                          "Switzerland" : "Berne"
                        }

# Print the entire dictionary
print("12 countries and their capitals: ")
print(country_capital_dict)

# Access and print the capital of the 5th country
print()
print("Capital of the 5th country: ")
print(country_capital_dict['Thailand'])

# Update the capital of the 8th country
country_capital_dict['Iceland'] = 'Kópavogur'
print()
print("Updated capital of the 8th country: ")
print(country_capital_dict)

# Delete the 11th country from the dictionary
del country_capital_dict['United States of America']
print()
print("Updated dictionary after deleting 11th country: ")
print(country_capital_dict)

# Print the last key-value pair in the dictionary
print()
last_key = list(country_capital_dict.keys())[-1]
last_value = country_capital_dict[last_key]
print("The last key-value pair is: ")
print(last_key, ":" ,last_value)