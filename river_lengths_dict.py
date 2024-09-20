# river_lengths_dict.py

# Dictionary of 6 rivers and their lengths in kilometers
river_lengths_dict = {
                        "Nile" : "6,650 km",
                        "Amazon River" : "6,400 km",
                        "Yangtze" : "6,300 km",
                        "Mississippi River" : "5,971 km",
                        "Yenisei River" : "5,540 km",
                        "Yellow River" : "5,464 km"
                      }

# Print the entire dictionary
print("6 rivers and their lengths in kilometers: ")
print(river_lengths_dict)

# Access and print the length of the 2nd river
print()
print("Length of the 2nd river: ")
print(river_lengths_dict['Amazon River'])

# Update the length of the 5th river
river_lengths_dict['Yenisei River'] = '5,550 km'
print()
print("Updated length of the 5th river: ")
print(river_lengths_dict)

# Delete the 4th river from the dictionary
del river_lengths_dict['Mississippi River']
print()
print("Updated dictionary after deleting 4th river: ")
print(river_lengths_dict)

# Print the last key-value pair in the dictionary
print()
last_key = list(river_lengths_dict.keys())[-1]
last_value = river_lengths_dict[last_key]
print("The last key-value pair is: ")
print(last_key, ":" ,last_value)