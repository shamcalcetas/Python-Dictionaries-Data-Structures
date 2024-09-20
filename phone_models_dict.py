# phone_models_dict.py

# Dictionary of 10 phone models and their manufacturers
phone_models_dict = {
                      "Galaxy S24 Ultra" : "Samsung Electronics",
                      "Pixel 8 Pro" : "Google Pixel",
                      "Xiaomi 14 Ultra" : "Xiaomi Global",
                      "iPhone 15 Pro" : "Apple Inc.",
                      "OnePlus Nord 4" : "OnePlus",
                      "Motorola Razr 50 Ultra" : "Motorola Mobility",
                      "Huawei Pura 70 Ultra" : "HUAWEI PHONES",
                      "Nokia XR20" : "HMD",
                      "CMF Phone 1" : "Nothing",
                      "Sony Xperia 1 VI" : "Sony"
                     }

# Print the entire dictionary
print("10 phone models and their manufacturers: ")
print(phone_models_dict)

# Access and print the manufacturer of the 2nd phone model
print()
print("Manufacturer of the 2nd phone model: ")
print(phone_models_dict['Pixel 8 Pro'])

# Update the manufacturer of the 8th phone model
phone_models_dict['Nokia XR20'] = 'HMD Global Oy'
print()
print("Updated manufacturer of the 8th phone model: ")
print(phone_models_dict)

# Delete the 6th phone model from the dictionary
del phone_models_dict['Motorola Razr 50 Ultra']
print()
print("Updated dictionary after deleting 6th phone model: ")
print(phone_models_dict)

# Print the last key-value pair in the dictionary
print()
last_key = list(phone_models_dict.keys())[-1]
last_value = phone_models_dict[last_key]
print("The last key-value pair is: ")
print(last_key, ":" ,last_value)