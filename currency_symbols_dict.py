# currency_symbols_dict.py

# Dictionary of 10 currencies and their symbols
currency_symbols_dict = {
                          "South Korean won" : "₩",
                          "Philippine peso" : "₱",
                          "Japanese yen" : "¥",
                          "Indian Rupee" : " ₹",
                          "United States dollar" : "$",
                          "Thai Baht" : "฿",
                          "Euro" : " €",
                          "Turkish lira" : "₺",
                          "Saudi Riyal" : "﷼",
                          "British pound sterling" : "£"
                        }

# Print the entire dictionary
print("10 currencies and their symbols: ")
print(currency_symbols_dict)

# Access and print the symbol of the 5th currency
print()
print("Symbol of the 5th currency: ")
print(currency_symbols_dict['United States dollar'])

# Update the symbol of the 9th currency
currency_symbols_dict['Saudi Riyal'] = 'س'
print()
print("Updated symbol of the 9th currency: ")
print(currency_symbols_dict)

# Delete the 3rd currency from the dictionary
del currency_symbols_dict['Japanese yen']
print()
print("Updated dictionary after deleting 3rd currency: ")
print(currency_symbols_dict)

# Print the last key-value pair in the dictionary
print()
last_key = list(currency_symbols_dict.keys())[-1]
last_value = currency_symbols_dict[last_key]
print("The last key-value pair is: ")
print(last_key, ":" ,last_value)