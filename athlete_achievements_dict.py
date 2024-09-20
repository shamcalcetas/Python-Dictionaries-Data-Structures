# athlete_achievements_dict.py

# Dictionary of 8 athletes and their greatest achievements
athlete_achievements_dict = {
                              "Vitaly Scherbo" : "Six gold medals",
                              "Jesse Owens" : "Four Olympic gold medals",
                              "Kurt Browning" : "Four-time world champion",
                              "Haile Gebreselassie" : "Greatest distance runner",
                              "Nadia Comaneci" : "Perfect 10 in gymnast",
                              "Roger Bannister" : "Four-minute mile",
                              "Michael Phelps" : "22 Olympic medals",
                              "Usain Bolt" : "The triple-double",
                            }

# Print the entire dictionary
print("8 athletes and their greatest achievements: ")
print(athlete_achievements_dict)

# Access and print the achievement of the 5th athlete
print()
print("Achievement of the 5th athlete: ")
print(athlete_achievements_dict['Nadia Comaneci'])

# Update the achievement of the 3rd athlete
athlete_achievements_dict['Kurt Browning'] = 'The first quad'
print()
print("Updated achievement of the 3rd athlete: ")
print(athlete_achievements_dict)

# Delete the 7th athlete from the dictionary
del athlete_achievements_dict['Michael Phelps']
print()
print("Updated dictionary after deleting 7th athlete: ")
print(athlete_achievements_dict)

# Print the last key-value pair in the dictionary
print()
last_key = list(athlete_achievements_dict.keys())[-1]
last_value = athlete_achievements_dict[last_key]
print("The last key-value pair is: ")
print(last_key, ":" ,last_value)