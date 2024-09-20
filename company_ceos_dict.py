# company_ceos_dict.py

# Dictionary of 10 companies and their current CEOs
company_ceos_dict = {
                      "Accenture" : "Julie Sweet",
                      "Alibaba" : "Eddie Wu",
                      "Amazon" : "Andy",
                      "Adobe Systems" : "Shantanu Narayen",
                      "Facebook" : "Mark Zuckerberg",
                      "Starbucks" : "Brian Niccol",
                      "Samsung" : "Oh-Hyun Kwon",
                      "SC Johnson" : "Herbert Fisk Johnson III",
                      "Dell" : "Michael Dell",
                      "Coca-Cola" : "James Quincey"
                        }

# Print the entire dictionary
print("10 companies and their current CEOs: ")
print(company_ceos_dict)

# Access and print the CEO of the 6th company
print()
print("CEO of the 6th company: ")
print(company_ceos_dict['Starbucks'])

# Update the CEO of the 3rd company
company_ceos_dict['Amazon'] = 'Andy Jassy'
print()
print("Updated CEO of the 3rd company: ")
print(company_ceos_dict)

# Delete the 9th company from the dictionary
del company_ceos_dict['Dell']
print()
print("Updated dictionary after deleting 9th company: ")
print(company_ceos_dict)

# Print the last key-value pair in the dictionary
print()
last_key = list(company_ceos_dict.keys())[-1]
last_value = company_ceos_dict[last_key]
print("The last key-value pair is: ")
print(last_key, ":" ,last_value)