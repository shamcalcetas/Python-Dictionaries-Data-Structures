# animal_sounds_dict.py

# Dictionary of 8 animals and their corresponding sounds
animal_sounds_dict = {
                        "Lion" : "Roar",
                        "Cat" : "Meow",
                        "Duck" : "Quack",
                        "Sheep" : "Baah",
                        "Bee" : "Buzz",
                        "Cow" : "Moo",
                        "Dog" : "Woof",
                        "Pig" : "Oink"
                      }

# Print the entire dictionary
print("8 animals and their corresponding sounds: ")
print(animal_sounds_dict)

# Access and print the sound of the 4th animal
print()
print("Sound of the 4th animal: ")
print(animal_sounds_dict['Sheep'])

# Update the sound of the 7th animal
animal_sounds_dict['Dog'] = 'Bark'
print()
print("Updated sound of the 7th animal: ")
print(animal_sounds_dict)

# Delete the 5th animal from the dictionary
del animal_sounds_dict['Bee']
print()
print("Updated dictionary after deleting 5th animal: ")
print(animal_sounds_dict)

# Print the last key-value pair in the dictionary
print()
last_key = list(animal_sounds_dict.keys())[-1]
last_value = animal_sounds_dict[last_key]
print("The last key-value pair is: ")
print(last_key, ":" ,last_value)