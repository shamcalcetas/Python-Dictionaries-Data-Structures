# city_landmarks_dict.py

# Dictionary of 8 cities and their famous landmarks
city_landmarks_dict = {
                        "Paris" : "Eiffel Tower",
                        "Siem Reap" : "Angkor Wat",
                        "Rome" : "Colosseum",
                        "Francisco" : "Golden Gate Bridge",
                        "London" : "Big Ben",
                        "Sydney" : "Sydney Opera House",
                        "New York" : "Statue of Liberty",
                        "Honshu" : "Mount Fuji"
                      }

# Print the entire dictionary
print("8 cities and their famous landmarks: ")
print(city_landmarks_dict)

# Access and print the landmark of the 6th city
print()
print("Landmark of the 6th city: ")
print(city_landmarks_dict['Sydney'])

# Update the landmark of the 2nd city
city_landmarks_dict['Siem Reap'] = 'Ta Prohm Temple'
print()
print("Updated landmark of the 2nd city: ")
print(city_landmarks_dict)

# Delete the 7th city from the dictionary
del city_landmarks_dict['New York']
print()
print("Updated dictionary after deleting 7th city: ")
print(city_landmarks_dict)

# Print the last key-value pair in the dictionary
print()
last_key = list(city_landmarks_dict.keys())[-1]
last_value = city_landmarks_dict[last_key]
print("The last key-value pair is: ")
print(last_key, ":" ,last_value)