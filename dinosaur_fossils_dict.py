# dinosaur_fossils_dict.py

# Dictionary of 7 dinosaurs and where their fossils were found
dinosaur_fossils_dict = {
                          "Tyrannosaurus Rex" : "Montana, USA",
                          "Triceratops" : "Montan, USA",
                          "Stegosaurus" : "Utah, USA",
                          "Velociraptor" : "Mongolia, Asia",
                          "Brachiosaurus" : "Colorado, USA",
                          "Parasaurolophus" : "Mexico, USA",
                          "Diplodocus" : "Wyoming, USA"
                        }

# Print the entire dictionary
print("7 dinosaurs and where their fossils were found: ")
print(dinosaur_fossils_dict)

# Access and print the location of the 4th dinosaur's fossils
print()
print("Location of the 4th dinosaur's fossils: ")
print(dinosaur_fossils_dict['Velociraptor'])

# Update the location of the 2nd dinosaur's fossils
dinosaur_fossils_dict['Triceratops'] = 'South Dakota, USA'
print()
print("Updated location of the 2nd dinosaur's fossils: ")
print(dinosaur_fossils_dict)

# Delete the 6th dinosaur from the dictionary
del dinosaur_fossils_dict['Parasaurolophus']
print()
print("Updated dictionary after deleting 6th dinosaur: ")
print(dinosaur_fossils_dict)

# Print the last key-value pair in the dictionary
print()
last_key = list(dinosaur_fossils_dict.keys())[-1]
last_value = dinosaur_fossils_dict[last_key]
print("The last key-value pair is: ")
print(last_key, ":" ,last_value)