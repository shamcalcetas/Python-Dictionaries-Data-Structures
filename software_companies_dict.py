# software_companies_dict.py

# Dictionary of 10 software companies and their headquarters
software_companies_dict = {
                            "Microsoft" : "Redmond, Washington, US",
                            "Google" : "Mountain View, California, US",
                            "Oracle" : "Austin, Texas, US",
                            "Salesforce" : "San Francisco, California, US",
                            "SAP" : "Walldorf, Germany",
                            "Adobe" : "San Jose, California, US",
                            "Intuit" : "Palo Alto, California, US",
                            "IBM" : "US",
                            "ServiceNow" : "Santa Clara, California, US",
                            "ADP" : "Roseland, New Jersey, US"
                          }

# Print the entire dictionary
print("10 software companies and their headquarters: ")
print(software_companies_dict)

# Access and print the headquarter of the 3rd company
print()
print("Headquarter of the 3rd company: ")
print(software_companies_dict['Oracle'])

# Update the headquarter of the 8th company
software_companies_dict['IBM'] = 'Armonk, New York, US'
print()
print("Updated headquarter of the 8th company: ")
print(software_companies_dict)

# Delete the 9th company from the dictionary
del software_companies_dict['ServiceNow']
print()
print("Updated dictionary after deleting 9th company: ")
print(software_companies_dict)

# Print the last key-value pair in the dictionary
print()
last_key = list(software_companies_dict.keys())[-1]
last_value = software_companies_dict[last_key]
print("The last key-value pair is: ")
print(last_key, ":" ,last_value)