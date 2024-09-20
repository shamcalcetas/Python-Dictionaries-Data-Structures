# university_courses_dict.py

# Dictionary of 8 universities and their popular courses
university_courses_dict = {
                            "Harvard University" : "Accounting & Finance",
                            "Royal College of Art" : "Art & Design",
                            "University of Oxford" : "African & Middle Eastern Studies",
                            "Yale University" : "Economics",
                            "Stanford University" : "Computer Science",
                            "New York University" : "Visual and Performing Arts",
                            "University of the Philippines Diliman" : "Business Administration",
                            "Massachusetts Institute of Technology" : "Mechanical Engineering"
                          }

# Print the entire dictionary
print("8 universities and their popular courses: ")
print(university_courses_dict)

# Access and print the course of the 3rd university
print()
print("Course of the 3rd university: ")
print(university_courses_dict['University of Oxford'])

# Update the course of the 5th university
university_courses_dict['Stanford University'] = 'Human Biology'
print()
print("Updated course of the 5th university: ")
print(university_courses_dict)

# Delete the 7th university from the dictionary
del university_courses_dict['University of the Philippines Diliman']
print()
print("Updated dictionary after deleting 7th university: ")
print(university_courses_dict)

# Print the last key-value pair in the dictionary
print()
last_key = list(university_courses_dict.keys())[-1]
last_value = university_courses_dict[last_key]
print("The last key-value pair is: ")
print(last_key, ":" ,last_value)