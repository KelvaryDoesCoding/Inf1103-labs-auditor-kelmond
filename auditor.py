#Variables
stock_quantity = 0 #Initialize to zero
failed_entries = 0

#Validation
def add_stock(stock_quantity, failed_entries):
    while stock_quantity < 500:
        stock_input = input("Please enter stock quantity: ") #Ensures value is an integer

        # User exits program check
        if stock_input.lower() == "quit":
            print(f"Total units processed: {stock_quantity}")
            print(f"Total failed entries: {failed_entries}")
            break

        # Integer check
        if not stock_input.isdigit():
            print("Error: Please enter a valid integer!")
            failed_entries += 1
            continue
        
        # Convert stock_input to integer after "Quit" string has been checked
        stock_input = int(stock_input)

        # Overstock check
        if stock_quantity + stock_input > 500:
            print("Alert: Inventory has exceeded 500 units!")
            break

        # Negative value check
        if stock_input < 0:
            print("Error: Please enter a positive integer!")
            stock_quantity -= stock_input
            failed_entries += 1
            continue

        stock_quantity += stock_input
        print(f"Total inventory is {stock_quantity} units")

# Call function
add_stock(stock_quantity, failed_entries)
