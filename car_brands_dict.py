# car_brands_dict.py

# Dictionary of 10 car brands and their country of origin
car_brands_dict = {
                    "Volvo" : "Sweden",
                    "Volkswagen" : "Germany",
                    "Toyota" : "Japan",
                    "Ford" : "USA",
                    "Mercedes-Benz" : "Germany",
                    "BMW" : "Germany",
                    "Kia" : "Korea",
                    "Audi" : "Germany",
                    "Mazda" : "Japan",
                    "Tesla" : "USA"
                  }

# Print the entire dictionary
print("10 car brands and their country of origin: ")
print(car_brands_dict)

# Access and print the country of origin of the 3rd car brand
print()
print("Country of origin of the 3rd car brand: ")
print(car_brands_dict['Toyota'])

# Update the country of origin of the 7th car brand
car_brands_dict['Kia'] = 'South Korea'
print()
print("Updated country of origin of the 7th car brand: ")
print(car_brands_dict)

# Delete the 8th car brand from the dictionary
del car_brands_dict['Audi']
print()
print("Updated dictionary after deleting 8th car brand: ")
print(car_brands_dict)

# Print the last key-value pair in the dictionary
print()
last_key = list(car_brands_dict.keys())[-1]
last_value = car_brands_dict[last_key]
print("The last key-value pair is: ")
print(last_key, ":" ,last_value)