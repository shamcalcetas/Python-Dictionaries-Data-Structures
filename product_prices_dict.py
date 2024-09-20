# product_prices_dict.py

# Dictionary of 10 products and their prices
product_prices_dict = {
                        "Reno Liver Spread | 85g" : "₱25.00",
                        "Purefoods Corned Beef | 150g" : "₱79.00",
                        "Libby's Vienna Sausage | 4.6oz" : "₱56.50",
                        "555 Tuna Afritada | 155g" : "₱26.75",
                        "Argentina Meat Loaf | 170g" : "₱23.50",
                        "Jolly Whole Corn Kernels | 425g" : "₱42.50",
                        "Seoul Kimchi Chinese Cabbage | 410g" : "₱170.00",
                        "Whole Kernel Corn | 425g" : "₱41.50",
                        "Ram Sweet Relish Pickles Sup | 100g" : "₱37.50",
                        "Hunt's Chili Beef And Beans | 100g" : "₱19.25"
                      }

# Print the entire dictionary
print("10 products and their prices: ")
print(product_prices_dict)

# Access and print the price of the 4th product
print()
print("Price of the 4th product: ")
print(product_prices_dict['555 Tuna Afritada | 155g'])

# Update the price of the 9th product
product_prices_dict['Ram Sweet Relish Pickles Sup | 100g'] = '₱35.50'
print()
print("Updated price of the 9th product: ")
print(product_prices_dict)

# Delete the 6th product from the dictionary
del product_prices_dict['Jolly Whole Corn Kernels | 425g']
print()
print("Updated dictionary after deleting 6th product: ")
print(product_prices_dict)

# Print the last key-value pair in the dictionary
print()
last_key = list(product_prices_dict.keys())[-1]
last_value = product_prices_dict[last_key]
print("The last key-value pair is: ")
print(last_key, ":" ,last_value)