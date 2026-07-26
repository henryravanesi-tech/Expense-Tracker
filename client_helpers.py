from datetime import date

def get_expense_id():
    cont = True 
    while cont:
        try:
            print("Please enter an expense_id: ", end='')
            expense_id = int(input().strip())
            cont = False
        except ValueError:
            print("You did not enter an integer, please try again.")
    return expense_id

def get_category():
    cont = True 
    while cont:
        print("Please enter a category: ", end='')
        cat = input().strip()
        if cat:
            cont = False
        else:
            print("No category entered, please try again.")
    return cat

def get_name():
    cont = True 
    while cont:
        print("Please enter a name: ", end='')
        name = input().strip()
        if name:
            cont = False
        else:
            print("No name entered, please try again.")
    return name

def get_amount():
    cont = True
    while cont:
        print("Please enter an amount for the expense: ", end='')
        try:
            amount = float(input().strip())
            if amount <=0:
                raise ValueError
            cont = False
        except ValueError:
            print("You did not enter a positive number, please try again.")
    return amount 

def get_date():
    cont = True
    while cont:
        print("Please enter a date for the expense (YYYY-MM-DD): ", end='')
        try:
            date_entered = date.fromisoformat(input().strip())
            date_text = date.isoformat(date_entered)
            cont = False
        except ValueError:
            print("You did not enter a valid date, please try again.")
    return date_text

def get_min_amount():
    cont = True
    while cont:
        print("Please enter a minimum amount: ", end='')
        try:
            amount = float(input().strip())
            if amount <=0:
                raise ValueError
            cont = False
        except ValueError:
            print("You did not enter a positive number, please try again.")
    return amount 

def get_max_amount():
    cont = True
    while cont:
        print("Please enter a maximum amount: ", end='')
        try:
            amount = float(input().strip())
            if amount <=0:
                raise ValueError
            cont = False
        except ValueError:
            print("You did not enter a positive number, please try again.")
    return amount 

def get_start_date():
    cont = True
    while cont:
        print("Please enter a start date (YYYY-MM-DD): ", end='')
        try:
            date_entered = date.fromisoformat(input().strip())
            date_text = date.isoformat(date_entered)
            cont = False
        except ValueError:
            print("You did not enter a valid date, please try again.")
    return date_text

def get_end_date():
    cont = True
    while cont:
        print("Please enter an end date (YYYY-MM-DD): ", end='')
        try:
            date_entered = date.fromisoformat(input().strip())
            date_text = date.isoformat(date_entered)
            cont = False
        except ValueError:
            print("You did not enter a valid date, please try again.")
    return date_text