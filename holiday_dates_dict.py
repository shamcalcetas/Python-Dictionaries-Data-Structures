# holiday_dates_dict.py

# Dictionary of 10 holidays and their corresponding dates
holiday_dates_dict = {
                        "New Year's Day" : "January 1",
                        "National Heroes Day" : "August 29",
                        "Bonifacio Day" : "November 30",
                        "Rizal Day" : "December 30",
                        "Independence Day" : "June 12",
                        "Araw ng Kagitingan" : "April 9",
                        "Labor Day" : "May 1",
                        "Good Friday" : "March 29",
                        "Maundy Thursday" : "March 28",
                        "Christmas Day" : "December 25"
                      }

# Print the entire dictionary
print("10 holidays and their corresponding dates: ")
print(holiday_dates_dict)

# Access and print the date of the 4th holiday
print()
print("Date of the 4th holiday: ")
print(holiday_dates_dict['Rizal Day'])

# Update the date of the 9th holiday
holiday_dates_dict['Maundy Thursday'] = 'March 29'
print()
print("Updated date of the 9th holiday: ")
print(holiday_dates_dict)

# Delete the 2nd holiday from the dictionary
del holiday_dates_dict['National Heroes Day']
print()
print("Updated dictionary after deleting 2nd holiday: ")
print(holiday_dates_dict)

# Print the last key-value pair in the dictionary
print()
last_key = list(holiday_dates_dict.keys())[-1]
last_value = holiday_dates_dict[last_key]
print("The last key-value pair is: ")
print(last_key, ":" ,last_value)