def check_price(item_number):
    if item_number <= 107:
        print("Price is $1.75")
        return (1.75)
    elif item_number => 201 and item_number <=304:
        #only the first 4 items are $0.50
        print("Price is $0.50")
        return (0.50)
    else:
        print("price is $0.25")
        return (0.25)