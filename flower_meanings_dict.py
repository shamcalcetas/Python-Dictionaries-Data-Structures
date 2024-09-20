# flower_meanings_dict.py

# Dictionary of 8 flowers and their symbolic meanings
flower_meanings_dict = {
                          "Rose" : "Love",
                          "Sunflower" : "Loyalty",
                          "Dahlia" : "Dignity",
                          "Orchid" : "Refined Beauty",
                          "Lion Heart" : "Bravery",
                          "Snowdrop" : "Hope",
                          "Hyacinth" : "Jealousy",
                          "Lily" : "Sweetness"
                      }

# Print the entire dictionary
print("8 flowers and their symbolic meanings: ")
print(flower_meanings_dict)

# Access and print the meaning of the 5th flower
print()
print("Meaning of the 5th flower: ")
print(flower_meanings_dict['Lion Heart'])

# Update the meaning of the 7th flower
flower_meanings_dict['Hyacinth'] = 'Forgiveness'
print()
print("Updated meaning of the 7th flower: ")
print(flower_meanings_dict)

# Delete the 6th flower from the dictionary
del flower_meanings_dict['Snowdrop']
print()
print("Updated dictionary after deleting 6th flower: ")
print(flower_meanings_dict)

# Print the last key-value pair in the dictionary
print()
last_key = list(flower_meanings_dict.keys())[-1]
last_value = flower_meanings_dict[last_key]
print("The last key-value pair is: ")
print(last_key, ":" ,last_value)