TICKET_PRICE = 10
SERVICE_CHARGE = 2

tickets_remaining = 100  

def price_total(number):
    return (TICKET_PRICE * number) + SERVICE_CHARGE

while tickets_remaining:
    print("There are {} tickets remaining.".format(tickets_remaining))
    name = input("\nWhat is your full name?\n")
    try:
        tickets_required = int(input("\nHi {}. How many tickets would you like to purchase today?\n".format(name)))
        if tickets_required > tickets_remaining:
            raise ValueError("There are only {} tickets available for purchase".format(tickets_remaining))
    except ValueError as err:
        print("Oh no, We ran into an issue. {}. Please try again".format(err))
    else:
        total_price = price_total(tickets_required)
        print("\nYour order total is £{}\n".format(total_price))
        confirmation = input("\nPlease enter 'Y' if you would like to proceed:\n")
        if confirmation.upper() == 'Y':
            print("\nSOLD! Thanks for your purchase, {}. Have a good day!".format(name))
            tickets_remaining -= tickets_required        
        else:
            print("\nNo worries. Hope to see you again soon! Thanks and Have a Good Day, {}\n".format(name))
print("Sorry {}. All tickets are sold out".format(name))
    
    