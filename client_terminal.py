import requests
from datetime import date

base_url = "http://127.0.0.1:8000"

def menu() -> int:
    
    print("1. Check api status")
    print("2. View all expenses")
    print("3. Search expenses by category")
    print("4. Get one expense by ID")
    print("5. Add a new expense")
    print("6. Modify/update a part of an expense")
    print("7. Fully Replace a specific expense")
    print("8. Delete a specific expense")
    print("9. Exit")
    
    while True:
        try:
            print("Please select a number: ", end='')
            choice = int(input().strip())
            if choice >= 1 and choice <= 9:
                return choice
            else:
                print("Invalid input, please try again.")
        except ValueError:
            print("Invalid input, please try again.")


def check_api_status() -> None:
    response = requests.get(base_url + "/")

    print("Status code: ", response.status_code)
    print("Response:", response.json())


def get_all_expenses() -> None:
    response = requests.get(base_url + "/expenses")
    expenses = response.json()
    
    print("Status code: ", response.status_code)
    print("Response: ", expenses)


def get_cat_expenses() -> None:
    cont = True 
    while cont:
        print("Please enter a category to search by: ", end='')
        cat = input().strip()
        if cat:
            cont = False
        else:
            print("No category entered, please try again.")

    response = requests.get(base_url + "/expenses", params={"category": cat})
    cat_expenses = response.json()
    print("Status code: ", response.status_code)
    print("Response: ", cat_expenses)


def get_specific_expense() -> None:
    cont = True 
    while cont:
        try:
            print("Please enter an expense_id: ", end='')
            expense_id = int(input().strip())
            cont = False
        except ValueError:
            print("You did not enter a integer, please try again.")
    
    response = requests.get(base_url + f"/expenses/{expense_id}")
    expense = response.json()

    print("Status code: ", response.status_code)
    print("Response: ", expense)


def add_new_expense() -> None:
    new_expense = {}
    name_l = True
    amount_l = True 
    category_l = True 
    date_l = True 

    while name_l:
        print("Please enter a name for the expense: ", end='')
        name = input().strip()
        if name:
            new_expense["name"] = name
            name_l = False
        else:
            print("No name entered, please try again.")

    while amount_l:
        print("Please enter an amount for the expense: ", end='')
        try:
            amount = float(input().strip())
            if amount <=0:
                raise ValueError
            new_expense["amount"] = amount
            amount_l = False
        except ValueError:
            print("You did not enter a positive number, please try again.")
        
    while category_l:
        print("Please enter a category for the expense: ", end='')
        category = input().strip()
        if category:
            new_expense["category"] = category
            category_l = False
        else: 
            print("No category entered, please try again.")

    while date_l:
        print("Please enter a date for the expense (YYYY-MM-DD): ", end='')
        try:
            date_entered = date.fromisoformat(input().strip())
            date_text = date.isoformat(date_entered)
            new_expense["date"] = date_text
            date_l = False
        except ValueError:
            print("You did not enter a valid date, please try again.")

    response = requests.post(base_url + "/expenses", json=new_expense)
    print("Status code: ", response.status_code)
    print("Response: ", response.json())

    
def update_existing_expense() -> None:
    update = {}
    cont = True
    int_cont = True 


    while int_cont:
        try:
            print("Please enter the expense id you wish to update: ", end='')
            expense_id = int(input().strip())
            int_cont = False
        except ValueError:
            print("You did not enter a integer, please try again.")

    print("Please select what categories you wish to update, continue will send through the request.")
    
    while cont:
        try:
            print("1. name")
            print("2. amount")
            print("3. category")
            print("4. date")
            print("5. continue (sends through request)")
            print("Choice: ", end='')
            choice = int(input().strip())

            if choice >= 1 and choice <= 5:
                name_l = True
                amount_l = True 
                category_l = True 
                date_l = True 
                if choice == 1:
                  while name_l:
                    print("Please enter a name for the expense: ", end='')
                    name = input().strip()
                    if name:
                        update["name"] = name
                        name_l = False
                    else:
                        print("No name entered, please try again.")
        
                elif choice == 2:
                    while amount_l:
                        print("Please enter an amount for the expense: ", end='')
                        try:
                            amount = float(input().strip())
                            if amount <=0:
                                raise ValueError
                            update["amount"] = amount
                            amount_l = False
                        except ValueError:
                            print("You did not enter a positive number, please try again.")
                elif choice == 3:
                    while category_l:
                        print("Please enter a category for the expense: ", end='')
                        category = input().strip()
                        if category:
                            update["category"] = category
                            category_l = False
                        else: 
                            print("No category entered, please try again.")
                elif choice == 4:
                    while date_l:
                        print("Please enter a date for the expense (YYYY-MM-DD): ", end='')
                        try:
                            date_entered = date.fromisoformat(input().strip())
                            date_text = date.isoformat(date_entered)
                            update["date"] = date_text
                            date_l = False
                        except ValueError:
                            print("You did not enter a valid date, please try again.")
                elif choice == 5:
                    cont = False
            else:
                raise ValueError
        except ValueError:
            print("Invalid input, please try again.")
    
    response = requests.patch(base_url + f"/expenses/{expense_id}", json=update)
    print("Status code: ", response.status_code)
    print("Response: ", response.json())

        
def replace_expense() -> None:
    replacement_expense = {}
    cont = True
    name_l = True
    amount_l = True 
    category_l = True 
    date_l = True 

    while cont:
        try:
            print("Please enter the expense id you wish to replace: ", end='')
            expense_id = int(input().strip())
            cont = False
        except ValueError:
            print("You did not enter a integer, please try again.")

    while name_l:
        print("Please enter a name for the expense: ", end='')
        name = input().strip()
        if name:
            replacement_expense["name"] = name
            name_l = False
        else:
            print("No name entered, please try again.")

    while amount_l:
        print("Please enter an amount for the expense: ", end='')
        try:
            amount = float(input().strip())
            if amount <=0:
                raise ValueError
            replacement_expense["amount"] = amount
            amount_l = False
        except ValueError:
            print("You did not enter a positive number, please try again.")
        
    while category_l:
        print("Please enter a category for the expense: ", end='')
        category = input().strip()
        if category:
            replacement_expense["category"] = category
            category_l = False
        else: 
            print("No category entered, please try again.")

    while date_l:
        print("Please enter a date for the expense (YYYY-MM-DD): ", end='')
        try:
            date_entered = date.fromisoformat(input().strip())
            date_text = date.isoformat(date_entered)
            replacement_expense["date"] = date_text
            date_l = False
        except ValueError:
            print("You did not enter a valid date, please try again.")

    response = requests.put(base_url + f"/expenses/{expense_id}", json=replacement_expense)
    print("Status code: ", response.status_code)
    print("Response: ", response.json())


def delete_expense() -> None:
    cont = True

    while cont:
        try:
            print("Please enter the expense id you wish to delete: ", end='')
            expense_id = int(input().strip())
            cont = False
        except ValueError:
            print("You did not enter a integer, please try again.")

    response = requests.delete(base_url + f"/expenses/{expense_id}")
    print("Status code: ", response.status_code)
    print("Response: ", response.json())


def main() -> None:
    cont = True
    print("Welcome to the expense tracker!")
    while cont:
        choice = menu()

        if choice == 1:
            check_api_status()
        
        elif choice == 2:
            get_all_expenses()

        elif choice == 3:
            get_cat_expenses()
        
        elif choice == 4:
            get_specific_expense()

        elif choice == 5:
            add_new_expense()
            
        elif choice == 6:
            update_existing_expense()

        elif choice == 7:
            replace_expense()

        elif choice == 8:
            delete_expense()

        elif choice == 9:
            cont = False
            print("done")


if __name__ == "__main__":
    main()