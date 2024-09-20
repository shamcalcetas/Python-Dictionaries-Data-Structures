# student_grades_dict.py

# Dictionary of 5 students and their corresponding grades
student_grades_dict = {
                        "Theo" : "B",
                        "John" : "C",
                        "Luna" : "A",
                        "Alex" : "B",
                        "Cora" : "C"
                      }

# Print the entire dictionary
print("5 students and their corresponding grades: ")
print(student_grades_dict)

# Access and print the grade of the 3rd student
print()
print("Grade of the 3rd student: ")
print(student_grades_dict['Luna'])

# Update the grade of the 2nd student
student_grades_dict['John'] = 'A'
print()
print("Updated grade of the 2nd student: ")
print(student_grades_dict)

# Delete the entry of the 5th student
del student_grades_dict['Cora']
print()
print("Updated dictionary after deleting 5th student: ")
print(student_grades_dict)

# Print the last key-value pair in the dictionary
print()
last_key = list(student_grades_dict.keys())[-1]
last_value = student_grades_dict[last_key]
print("The last key-value pair is: ")
print(last_key, ":" ,last_value)