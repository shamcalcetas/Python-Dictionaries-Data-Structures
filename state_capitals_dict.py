# state_capitals_dict.py

# Dictionary of 10 states and their capitals
state_capitals_dict = {
                        "Alaska" : "Juneau",
                        "California" : "Sacramento",
                        "Colorado" : "Denver",
                        "Florida" : "Tallahassee",
                        "Pennsylvania" : "Harrisburg",
                        "Hawaii" : "Honolulu",
                        "Kentucky" : "Frankfort",
                        "Maine" : "Augusta",
                        "Massachusetts" : "Boston",
                        "New Jersey" : "Trenton"
                      }

# Print the entire dictionary
print("10 states and their capitals: ")
print(state_capitals_dict)

# Access and print the capital of the 4th state
print()
print("Capital of the 4th state: ")
print(state_capitals_dict['Florida'])

# Update the capital of the 9th state
state_capitals_dict['Massachusetts'] = 'Springfield'
print()
print("Updated capital of the 9th state: ")
print(state_capitals_dict)

# Delete the 7th state from the dictionary
del state_capitals_dict['Kentucky']
print()
print("Updated dictionary after deleting 7th state: ")
print(state_capitals_dict)

# Print the last key-value pair in the dictionary
print()
last_key = list(state_capitals_dict.keys())[-1]
last_value = state_capitals_dict[last_key]
print("The last key-value pair is: ")
print(last_key, ":" ,last_value)