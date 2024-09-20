# author_books_dict.py

# Dictionary of 8 authors and their famous books
author_books_dict = {
                      "William Shakespeare" : "Macbeth",
                      "Lewis Carrol" : "Alice in Wonderland",
                      "Mark Twain" : "Adventures of Tom Sawyer",
                      "Jules Verne" : "Around the World in eighty days ",
                      "George Orwell" : "Animal Farm",
                      "Samuel Coleridge" : "Ancient Mariner",
                      "Charles Darwin" : "Origin of Species",
                      "E.M. Forster" : "A passage to India"
                    }

# Print the entire dictionary
print("8 authors and their famous books: ")
print(author_books_dict)

# Access and print the book of the 5th author
print()
print("Book of the 5th author: ")
print(author_books_dict['George Orwell'])

# Update the book of the 7th author
author_books_dict['Charles Darwin'] = 'The Voyage of the Beagle'
print()
print("Updated book of the 7th author: ")
print(author_books_dict)

# Delete the 6th author from the dictionary
del author_books_dict['Samuel Coleridge']
print()
print("Updated dictionary after deleting 6th author: ")
print(author_books_dict)

# Print the last key-value pair in the dictionary
print()
last_key = list(author_books_dict.keys())[-1]
last_value = author_books_dict[last_key]
print("The last key-value pair is: ")
print(last_key, ":" ,last_value)