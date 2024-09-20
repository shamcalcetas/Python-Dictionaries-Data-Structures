# space_telescope_missions_dict.py

# Dictionary of 5 space telescopes and their missions
space_telescope_missions_dict = {
                                  "Hubble" : "Capturing galaxies merging",
                                  "Spitzer" : "Detect light from an exoplanet",
                                  "Kepler" : "Observe one patch of the sky",
                                  "James Webb" : "Study how galaxies and stars change over cosmic time",
                                  "Chandra X-ray" : "Observe X-rays from high-energy regions of the universe",
                                }

# Print the entire dictionary
print("5 space telescopes and their missions: ")
print(space_telescope_missions_dict)

# Access and print the mission of the 3rd telescope
print()
print("Mission of the 3rd telescope: ")
print(space_telescope_missions_dict['Kepler'])

# Update the mission of the 1st telescope
space_telescope_missions_dict['Hubble'] = 'Probing the supermassive black holes that lurk in their depths'
print()
print("Updated mission of the 1st telescope: ")
print(space_telescope_missions_dict)

# Delete the 4th telescope from the dictionary
del space_telescope_missions_dict['James Webb']
print()
print("Updated dictionary after deleting 4th telescope: ")
print(space_telescope_missions_dict)

# Print the last key-value pair in the dictionary
print()
last_key = list(space_telescope_missions_dict.keys())[-1]
last_value = space_telescope_missions_dict[last_key]
print("The last key-value pair is: ")
print(last_key, ":" ,last_value)