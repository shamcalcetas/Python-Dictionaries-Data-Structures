# animal_habitats_dict.py

# Dictionary of 8 animals and their natural habitats
animal_habitats_dict = {
                          "Fox" : "Forest",
                          "Frog" : "Wetland",
                          "Kangaroo" : "Savanna",
                          "Polar Bear" : "Arctic Tundra",
                          "Giraffe" : "Grasslands",
                          "Turtles" : "Marine",
                          "Catfish" : "Freshwater",
                          "Camel" : "Desert"
                        }

# Print the entire dictionary
print("8 animals and their natural habitats: ")
print(animal_habitats_dict)

# Access and print the habitat of the 3rd animal
print()
print("Habitat of the 3rd animal: ")
print(animal_habitats_dict['Kangaroo'])

# Update the habitat of the 5th animal
animal_habitats_dict['Giraffe'] = 'Woodlands'
print()
print("Updated habitat of the 5th animal: ")
print(animal_habitats_dict)

# Delete the 7th animal from the dictionary
del animal_habitats_dict['Catfish']
print()
print("Updated dictionary after deleting 7th animal: ")
print(animal_habitats_dict)

# Print the last key-value pair in the dictionary
print()
last_key = list(animal_habitats_dict.keys())[-1]
last_value = animal_habitats_dict[last_key]
print("The last key-value pair is: ")
print(last_key, ":" ,last_value)