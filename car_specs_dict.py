# car_specs_dict.py

# Dictionary of 10 car models and their engine specifications
car_specs_dict = {
                    "Bugatti Chiron" : "1500 hp",
                    "Lamborghini Aventador" : "1600 hp",
                    "Hennessey Venom F5" : "1622 hp",
                    "SSC Tuatara" : "1774 hp",
                    "Pininfarina Battista" : "1900 hp",
                    "Rimac C_Two" : "1914 hp",
                    "Lotus Evija" : "2000 hp",
                    "Aspark Owl" : "2012 hp",
                    "Dagger GT" : "2028 hp",
                    "Devel Sixteen Engine Dyno" : "4515 hp"
                  }

# Print the entire dictionary
print("10 car models and their engine specifications: ")
print(car_specs_dict)

# Access and print the specifications of the 4th car model
print()
print("Specifications of the 4th car model: ")
print(car_specs_dict['SSC Tuatara'])

# Update the specifications of the 9th car model
car_specs_dict['Dagger GT'] = '2030 hp'
print()
print("Updated specifications of the 9th car model: ")
print(car_specs_dict)

# Delete the 5th car model from the dictionary
del car_specs_dict['Pininfarina Battista']
print()
print("Updated dictionary after deleting 5th car model: ")
print(car_specs_dict)

# Print the last key-value pair in the dictionary
print()
last_key = list(car_specs_dict.keys())[-1]
last_value = car_specs_dict[last_key]
print("The last key-value pair is: ")
print(last_key, ":" ,last_value)