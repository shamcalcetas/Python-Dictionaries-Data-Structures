# company_founders_dict.py

# Dictionary of 8 companies and their founders
company_founders_dict = {
                          "Samsung" : "Lee Byung-chul",
                          "Wipro" : "M.H. Premji",
                          "Amazon" : "Jeff Bezos",
                          "Ebay" : "Pierre Omidyar",
                          "Cap Gemini" : "Serge Kampf",
                          "Alibaba Group" : "Jack Ma",
                          "Dell" : "Michael Dell",
                          "Tata Consultancy Services Limited (TCS)" : "J.R.D Tata"
                        }

# Print the entire dictionary
print("8 companies and their founders: ")
print(company_founders_dict)

# Access and print the founder of the 6th company
print()
print("Founder of the 6th company: ")
print(company_founders_dict['Alibaba Group'])

# Update the founder of the 2nd company
company_founders_dict['Wipro'] = 'Azim Hashim Premji'
print()
print("Updated founder of the 2nd company: ")
print(company_founders_dict)

# Delete the 8th company from the dictionary
del company_founders_dict['Tata Consultancy Services Limited (TCS)']
print()
print("Updated dictionary after deleting 8th company: ")
print(company_founders_dict)

# Print the last key-value pair in the dictionary
print()
last_key = list(company_founders_dict.keys())[-1]
last_value = company_founders_dict[last_key]
print("The last key-value pair is: ")
print(last_key, ":" ,last_value)