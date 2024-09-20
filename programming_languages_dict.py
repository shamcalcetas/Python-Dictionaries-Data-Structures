# programming_languages_dict.py

# Dictionary of 7 programming languages and their developers
programming_languages_dict = {
                                "Python" : "Guido van Rossum",
                                "C#" : "A.Hejlsberg, S.Wiltamuth, & P.Golde",
                                "Java" : "James Gosling",
                                "HTML" : "Tim Berners-Lee",
                                "C++" : "Bjarne Stroustrup",
                                "SQL" : "Raymond Boyce",
                                "Rust" : "Graydon Hoare"
                            }

# Print the entire dictionary
print("7 programming languages and their developers: ")
print(programming_languages_dict)

# Access and print the developer of the 4th programming language
print()
print("Developer of the 4th programming language: ")
print(programming_languages_dict['HTML'])

# Update the developer of the 6th programming language
programming_languages_dict['SQL'] = 'Donald Chamberlin'
print()
print("Updated developer of the 6th programming language: ")
print(programming_languages_dict)

# Delete the 2nd programming language from the dictionary
del programming_languages_dict['C#']
print()
print("Updated dictionary after deleting 2nd programming language: ")
print(programming_languages_dict)

# Print the last key-value pair in the dictionary
print()
last_key = list(programming_languages_dict.keys())[-1]
last_value = programming_languages_dict[last_key]
print("The last key-value pair is: ")
print(last_key, ":" ,last_value)