# music_albums_dict.py

# Dictionary of 10 music albums and their release years
music_albums_dict = {
                      "Red" : "2012",
                      "1989" : "2023",
                      "Believe" : "2012",
                      "Empathy" : "2021",
                      "Episode" : "2021",
                      "Tanong" : "2023",
                      "Autumn Variations" : "2023",
                      "Layover" : "2023",
                      "Pasahili" : "2022",
                      "Timeless" : "2024"
                    }

# Print the entire dictionary
print("10 music albums and their release years: ")
print(music_albums_dict)

# Access and print the release year of the 3rd album
print()
print("Release year of the 3rd album: ")
print(music_albums_dict['Believe'])

# Update the release year of the 8th album
music_albums_dict['Layover'] = '2024'
print()
print("Updated release year of the 8th album: ")
print(music_albums_dict)

# Delete the 5th album from the dictionary
del music_albums_dict['Episode']
print()
print("Updated dictionary after deleting 5th album: ")
print(music_albums_dict)

# Print the last key-value pair in the dictionary
print()
last_key = list(music_albums_dict.keys())[-1]
last_value = music_albums_dict[last_key]
print("The last key-value pair is: ")
print(last_key, ":" ,last_value)