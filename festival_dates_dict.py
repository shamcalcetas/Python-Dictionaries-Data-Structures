# festival_dates_dict.py

# Dictionary of 10 festivals and their celebration dates
festival_dates_dict = {
                          "Sinulog Festival" : "January 15",
                          "Boryeong Mud Festival" : "July 21-30",
                          "Spring Festival" : "July 1 ",
                          "Pagoda Festival" : "July 4 - 7",
                          "Holi" : "Mar 25",
                          "Diwali" : "Oct. 15-21",
                          "White Nights Festival" : "May 26",
                          "Carnival of Venice" : "Feb. 11-28",
                          "Songkran Festival" : "April 13-15",
                          "La Tomatina" : "Aug. 30"
                      }

# Print the entire dictionary
print("10 festivals and their celebration dates: ")
print(festival_dates_dict)

# Access and print the date of the 3rd festival
print()
print("Date of the 3rd festival: ")
print(festival_dates_dict['Spring Festival'])

# Update the date of the 7th festival
festival_dates_dict['White Nights Festival'] = 'July 23'
print()
print("Updated date of the 7th festival: ")
print(festival_dates_dict)

# Delete the 5th festival from the dictionary
del festival_dates_dict['Holi']
print()
print("Updated dictionary after deleting 5th festival: ")
print(festival_dates_dict)

# Print the last key-value pair in the dictionary
print()
last_key = list(festival_dates_dict.keys())[-1]
last_value = festival_dates_dict[last_key]
print("The last key-value pair is: ")
print(last_key, ":" ,last_value)