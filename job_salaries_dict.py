# job_salaries_dict.py

# Dictionary of 10 jobs and their average salaries
job_salaries_dict = {
                      "Cardiologist" : "$243,759 per year",
                      "Anesthesiologist" : "$370,454 per year",
                      "Orthodontist" : "$294,259 per year",
                      "Psychiatrist" : "$255,958 per year",
                      "Surgeon" : "$297,626 per year",
                      "Physician" : "$214,096 per year",
                      "Dentist" : "$223,864 per year",
                      "Pediatrician" : "$166,984 per year",
                      "Optometrist" : "$145,632 per year",
                      "Nurse practitioner" : "$120,621 per year"
                    }

# Print the entire dictionary
print("10 jobs and their average salaries: ")
print(job_salaries_dict)

# Access and print the salary of the 3rd job
print()
print("Salary of the 3rd job: ")
print(job_salaries_dict['Orthodontist'])

# Update the salary of the 7th job
job_salaries_dict['Dentist'] = '$230,890 per year'
print()
print("Updated salary of the 7th job: ")
print(job_salaries_dict)

# Delete the 9th job from the dictionary
del job_salaries_dict['Optometrist']
print()
print("Updated dictionary after deleting 9th job: ")
print(job_salaries_dict)

# Print the last key-value pair in the dictionary
print()
last_key = list(job_salaries_dict.keys())[-1]
last_value = job_salaries_dict[last_key]
print("The last key-value pair is: ")
print(last_key, ":" ,last_value)