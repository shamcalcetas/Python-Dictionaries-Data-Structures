# movie_directors_dict.py

# Dictionary of 10 movies and their directors
movie_directors_dict = {
                          "Exit" : "Lee Sang-geun",
                          "Parasite" : "Bong Joon-ho",
                          "Titanic" : "James Cameron",
                          "Deadpool & Wolverine" : "Shawn Levy",
                          "The Witch: P1" : "Park Hoon-jung",
                          "Alive" : "Cho Il-hyung",
                          "The Roundup" : "Lee Sang-yong",
                          "Aquaman " : "James Wan",
                          "Ride On" : "Yang",
                          "Police Story" : "Jackie Chan"
                        }

# Print the entire dictionary
print("10 movies and their directors: ")
print(movie_directors_dict)

# Access and print the director of the 5th movie
print()
print("Director of the 5th movie: ")
print(movie_directors_dict['The Witch: P1'])

# Update the director of the 9th movie
movie_directors_dict['Ride On'] = 'Larry Yang'
print()
print("Updated director of the 9th movie: ")
print(movie_directors_dict)

# Delete the 7th movie from the dictionary
del movie_directors_dict['The Roundup']
print()
print("Updated dictionary after deleting 7th movie: ")
print(movie_directors_dict)

# Print the last key-value pair in the dictionary
print()
last_key = list(movie_directors_dict.keys())[-1]
last_value = movie_directors_dict[last_key]
print("The last key-value pair is: ")
print(last_key, ":" ,last_value)