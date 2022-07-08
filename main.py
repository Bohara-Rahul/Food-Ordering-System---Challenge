def main():
    restaurants_with_price = { 
            "Wild burger joint" :  15 ,
            "Awesome pizza place" :  25 ,
            "Crispy fries" :  10,
            "Hungry fried chicken" :  22 
        }
    
    food_input = input('Enter the food item: ')

    for name in restaurants_with_price.keys():
        if food_input.lower() in name.lower():
            print(name + ', ' + '$' + str(restaurants_with_price[name]))
    
main()