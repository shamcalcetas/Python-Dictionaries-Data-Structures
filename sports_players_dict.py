# sports_players_dict.py

# Dictionary of 10 sports and their most famous players
sports_players_dict = {
                        "Basketball" : "LeBron James",
                        "Football" : "Lionel Messi",
                        "Golf" : "Tiger Woods",
                        "Tennis" : "Roger Federer",
                        "Track and Field" : "Usain Bolt",
                        "Weightlifting" : "Diaz",
                        "Boxing" : "Manny Pacquiao",
                        "Bowling" : "Paeng Nepomuceno",
                        "Gymnastics" : "Carlos Yulo",
                        "Billiards" : "Efren “Bata” Reyes"
                      }

# Print the entire dictionary
print("10 sports and their most famous players: ")
print(sports_players_dict)

# Access and print the player of the 4th sport
print()
print("Player of the 4th sport: ")
print(sports_players_dict['Tennis'])

# Update the player of the 6th sport
sports_players_dict['Weightlifting'] = 'Hidilyn Diaz'
print()
print("Updated player of the 6th sport: ")
print(sports_players_dict)

# Delete the 10th sport from the dictionary
del sports_players_dict['Billiards']
print()
print("Updated dictionary after deleting 10th sport: ")
print(sports_players_dict)

# Print the last key-value pair in the dictionary
print()
last_key = list(sports_players_dict.keys())[-1]
last_value = sports_players_dict[last_key]
print("The last key-value pair is: ")
print(last_key, ":" ,last_value)