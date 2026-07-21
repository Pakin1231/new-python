
keep_going = 'y'
while keep_going.lower() == 'y':
    try:
        wholesale = float(input("Enter the item's wholesale cost: "))
    except ValueError:
        print('Invalid input. Please enter a numeric value.')
        continue

    # Calculate the retail price (markup factor 2.5).
    retail_price = wholesale * 2.5

    # Display the retail price.
    print(f'Retail price: ${retail_price:.2f}')

    # See if the user wants to do another one.
    keep_going = input('Do you have another item? (Enter y for yes): ')