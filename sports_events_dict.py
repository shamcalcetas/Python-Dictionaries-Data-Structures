# sports_events_dict.py

# Dictionary of 7 sports events and their corresponding years
sports_events_dict = {
                        "Paris Olympics" : "2024",
                        "Paris Paralympic Games" : "2024",
                        "FIFA Womens World Cup" : "2023",
                        "Batang Pinoy" : "2023",
                        "Winter Olympic" : "2022",
                        "Asian Para Games" : "2022",
                        "South East Asian Games" : "2019",
                      }

# Print the entire dictionary
print("7 sports events and their corresponding years: ")
print(sports_events_dict)

# Access and print the year of the 3rd sports event
print()
print("Year of the 3rd sports event: ")
print(sports_events_dict['FIFA Womens World Cup'])

# Update the year of the 6th sports event
sports_events_dict['Asian Para Games'] = '2021'
print()
print("Updated year of the 6th sports event: ")
print(sports_events_dict)

# Delete the 5th sports event from the dictionary
del sports_events_dict['Winter Olympic']
print()
print("Updated dictionary after deleting 5th sports event: ")
print(sports_events_dict)

# Print the last key-value pair in the dictionary
print()
last_key = list(sports_events_dict.keys())[-1]
last_value = sports_events_dict[last_key]
print("The last key-value pair is: ")
print(last_key, ":" ,last_value)