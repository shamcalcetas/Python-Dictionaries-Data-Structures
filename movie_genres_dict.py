# movie_genres_dict.py

# Dictionary of 8 movie genres and their corresponding example movies
movie_genres_dict = {
                      "Action" : "The Roundup",
                      "Horror" : "The Call",
                      "Crime" : "The Drug King",
                      "Comedy" : "The Odd Family",
                      "Sci-fi" : "Alienoid",
                      "Fantasy" : "A Werewolf Boy",
                      "Thriller" : "Unlocked",
                      "Sport" : "Dream"
                    }

# Print the entire dictionary
print("8 movie genres and their corresponding example movies: ")
print(movie_genres_dict)

# Access and print the example movie of the 3rd genre
print()
print("Example movie of the 3rd genre: ")
print(movie_genres_dict['Crime'])

# Update the example movie of the 5th genre
movie_genres_dict['Sci-fi'] = 'Psychokinesis'
print()
print("Updated example movie of the 5th genre: ")
print(movie_genres_dict)

# Delete the 7th genre from the dictionary
del movie_genres_dict['Thriller']
print()
print("Updated dictionary after deleting 7th genre: ")
print(movie_genres_dict)

# Print the last key-value pair in the dictionary
print()
last_key = list(movie_genres_dict.keys())[-1]
last_value = movie_genres_dict[last_key]
print("The last key-value pair is: ")
print(last_key, ":" ,last_value)