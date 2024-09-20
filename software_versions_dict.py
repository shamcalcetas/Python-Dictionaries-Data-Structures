# software_versions_dict.py

# Dictionary of 6 software programs and their latest versions
software_versions_dict = {
                            "Ms Office" : "2021",
                            "Adobe Photoshop" : "2024 ver. 25.12",
                            "NetBeans" : "2024 ver. 23",
                            "PyCharm" : "2024 ver. 2.2",
                            "Visual Studio Code" : "2024 ver. 1.93",
                            "Medibang Paint" : "2023 ver. 29.1",
                        }

# Print the entire dictionary
print("6 software programs and their latest versions: ")
print(software_versions_dict)

# Access and print the version of the 4th software
print()
print("Version of the 4th software: ")
print(software_versions_dict['PyCharm'])

# Update the version of the 2nd software
software_versions_dict['Adobe Photoshop'] = '2025 ver. 26.15'
print()
print("Updated version of the 2nd software: ")
print(software_versions_dict)

# Delete the 5th software from the dictionary
del software_versions_dict['Visual Studio Code']
print()
print("Updated dictionary after deleting 5th software: ")
print(software_versions_dict)

# Print the last key-value pair in the dictionary
print()
last_key = list(software_versions_dict.keys())[-1]
last_value = software_versions_dict[last_key]
print("The last key-value pair is: ")
print(last_key, ":" ,last_value)