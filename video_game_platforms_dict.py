# video_game_platforms_dict.py

# Dictionary of 8 video games and their platforms
video_game_platforms_dict = {
                              "Tony Hawk's Pro Skater 2" : "PlayStation",
                              "Forza Motorsport" : "Xbox",
                              "Super Mario Odyssey" : "Nintendo Switch",
                              "Street Fighter II" : "Arcade",
                              "Star Wars: Dark Forces" : "DOS",
                              "Bubble Bobble" : "MSX",
                              "Princess Maker 2" : "PC-98",
                              "Resident Evil 2" : "PlayStation 4"
                            }

# Print the entire dictionary
print("8 video games and their platforms: ")
print(video_game_platforms_dict)

# Access and print the platform of the 2nd video game
print()
print("Platform of the 2nd video game: ")
print(video_game_platforms_dict['Forza Motorsport'])

# Update the platform of the 6th video game
video_game_platforms_dict['Bubble Bobble'] = 'Arcade'
print()
print("Updated platform of the 6th video game: ")
print(video_game_platforms_dict)

# Delete the 4th video game from the dictionary
del video_game_platforms_dict['Street Fighter II']
print()
print("Updated dictionary after deleting 4th video game: ")
print(video_game_platforms_dict)

# Print the last key-value pair in the dictionary
print()
last_key = list(video_game_platforms_dict.keys())[-1]
last_value = video_game_platforms_dict[last_key]
print("The last key-value pair is: ")
print(last_key, ":" ,last_value)