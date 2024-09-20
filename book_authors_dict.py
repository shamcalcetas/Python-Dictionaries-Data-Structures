# book_authors_dict.py

# Dictionary of 12 books and their authors
book_authors_dict = {
                      "Macbeth" : "William Shakespeare",
                      "Alice in Wonderland" : "Lewis Carrol",
                      "Adventures of Tom Sawyer" : "Mark Twain",
                      "Around the World in eighty days" : "Jules Verne",
                      "Ancient Mariner" : "Coleridge",
                      "Animal Farm" : "George Orwell",
                      "Origin of Species" : "Charles Darwin",
                      "A passage to India" : "E.M.Forster",
                      "Time Machine" : "H.G. Wells",
                      "The Wild Iris" : "Louis Gluck",
                      "Adventures of Sherlock Holmes" : "Arthur Conan Doyle",
                      "Utopia" : "Thomas Moor"
                    }

# Print the entire dictionary
print("12 books and their authors: ")
print(book_authors_dict)

# Access and print the author of the 9th book
print()
print("Author of the 9th book: ")
print(book_authors_dict['Time Machine'])

# Update the author of the 5th book
book_authors_dict['Ancient Mariner'] = 'Samuel Taylor Coleridge'
print()
print("Updated author of the 5th book: ")
print(book_authors_dict)

# Delete the 3rd book from the dictionary
del book_authors_dict['Adventures of Tom Sawyer']
print()
print("Updated dictionary after deleting 3rd book: ")
print(book_authors_dict)

# Print the last key-value pair in the dictionary
print()
last_key = list(book_authors_dict.keys())[-1]
last_value = book_authors_dict[last_key]
print("The last key-value pair is: ")
print(last_key, ":" ,last_value)