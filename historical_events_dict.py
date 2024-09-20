# historical_events_dict.py

# Dictionary of 8 historical events and their years
historical_events_dict = {
                            "The Mughal Empire" : "1526-1857",
                            "The American Revolution" : "1765-1783",
                            "The French Revolution & Napoleonic Wars" : "1789-1815",
                            "World War 1" : "1914-1918",
                            "The Russian Revolution" : "1917-1923",
                            "The Third Reich" : "1924-1929",
                            "The Great Depression" : "1929-1941",
                            "World War II" : "1939-1945",
                          }

# Print the entire dictionary
print("8 historical events and their years: ")
print(historical_events_dict)

# Access and print the year of the 2nd event
print()
print("Year of the 2nd event: ")
print(historical_events_dict['The American Revolution'])

# Update the year of the 7th event
historical_events_dict['The Great Depression'] = '1930-1940'
print()
print("Updated year of the 7th event: ")
print(historical_events_dict)

# Delete the 5th event from the dictionary
del historical_events_dict['The Russian Revolution']
print()
print("Updated dictionary after deleting 5th event: ")
print(historical_events_dict)

# Print the last key-value pair in the dictionary
print()
last_key = list(historical_events_dict.keys())[-1]
last_value = historical_events_dict[last_key]
print("The last key-value pair is: ")
print(last_key, ":" ,last_value)