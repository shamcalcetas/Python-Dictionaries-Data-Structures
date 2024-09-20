# city_population_dict.py

# Dictionary of 10 cities and their corresponding population
city_population_dict = {
                          "Tokyo" : "37,115,035",
                          "Delhi" : "33,807,403",
                          "Shanghai" : "29,867,918",
                          "Dhaka" : "23,935,652",
                          "Sao Paulo" : "22,806,704",
                          "Cairo" : "22,623,874",
                          "Mexico City" : "22,505,315",
                          "Beijing" : "22,189,082",
                          "Mumbai" : "21,673,149",
                          "Osaka" : "18,967,459"
                        }

# Print the entire dictionary
print("10 cities and their corresponding population: ")
print(city_population_dict)

# Access and print the population of the 6th city
print()
print("Population of the 6th city: ")
print(city_population_dict['Cairo'])

# Update the population of the 3rd city
city_population_dict['Shanghai'] = '29,900,000'
print()
print("Updated population of the 3rd city: ")
print(city_population_dict)

# Delete the 9th city from the dictionary
del city_population_dict['Mumbai']
print()
print("Updated dictionary after deleting 9th city: ")
print(city_population_dict)

# Print the last key-value pair in the dictionary
print()
last_key = list(city_population_dict.keys())[-1]
last_value = city_population_dict[last_key]
print("The last key-value pair is: ")
print(last_key, ":" ,last_value)