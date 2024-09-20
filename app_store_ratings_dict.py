# app_store_ratings_dict.py

# Dictionary of 10 apps and their user ratings
app_store_ratings_dict = {
                            "Netflix" : "4.2",
                            "Instagram" : "4.2",
                            "Facebook" : "4.1",
                            "Messenger" : "4.0",
                            "SHEIN" : "4.1",
                            "ZALORA" : "4.8",
                            "Shopee" : "4.5",
                            "YouTube" : "4.3",
                            "Microsoft Outlook" : "4.7",
                            "Foodpanda" : "4.5"
                          }

# Print the entire dictionary
print("10 apps and their user ratings: ")
print(app_store_ratings_dict)

# Access and print the rating of the 6th app
print()
print("Rating of the 6th app: ")
print(app_store_ratings_dict['ZALORA'])

# Update the rating of the 8th app
app_store_ratings_dict['YouTube'] = '4.5'
print()
print("Updated rating of the 8th app: ")
print(app_store_ratings_dict)

# Delete the 9th app from the dictionary
del app_store_ratings_dict['Microsoft Outlook']
print()
print("Updated dictionary after deleting 9th app: ")
print(app_store_ratings_dict)

# Print the last key-value pair in the dictionary
print()
last_key = list(app_store_ratings_dict.keys())[-1]
last_value = app_store_ratings_dict[last_key]
print("The last key-value pair is: ")
print(last_key, ":" ,last_value)