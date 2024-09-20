# artist_songs_dict.py

# Dictionary of 8 artists and their top songs
car_specs_dict = {
                    "Taylor Swift" : "You Belong with Me",
                    "Justin Bieber" : "Love Yourself",
                    "Maki" : "Dilaw",
                    "Ed Sheeran" : "Perfect",
                    "Zack Tabudlo" : "Pano",
                    "Katy Perry" : "Roar",
                    "Meghan Trainor" : "All About That Bass",
                    "D.O." : "Rose"
                  }

# Print the entire dictionary
print("8 artists and their top songs: ")
print(car_specs_dict)

# Access and print the top song of the 3rd artist
print()
print("Top song of the 3rd artist: ")
print(car_specs_dict['Maki'])

# Update the top song of the 6th artist
car_specs_dict['Katy Perry'] = 'The One That Got Away'
print()
print("Updated top song of the 6th artist: ")
print(car_specs_dict)

# Delete the 7th artist from the dictionary
del car_specs_dict['Meghan Trainor']
print()
print("Updated dictionary after deleting 7th artist: ")
print(car_specs_dict)

# Print the last key-value pair in the dictionary
print()
last_key = list(car_specs_dict.keys())[-1]
last_value = car_specs_dict[last_key]
print("The last key-value pair is: ")
print(last_key, ":" ,last_value)