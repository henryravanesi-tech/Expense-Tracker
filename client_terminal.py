import requests

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
    print("Please enter a category to search by: ", end='')
    cat = input().strip()
    response = requests.get(base_url + "/expenses", params={"category": cat})
    cat_expenses = response.json()
    print("Status code: ", response.status_code)
    print("Response: ", cat_expenses)


def get_specific_expense() -> None:
    print("Please enter an expense_id: ", end='')
    expense_id = input().strip()
    
    response = requests.get(base_url + f"/expenses/{expense_id}")
    expense = response.json()

    print("Status code: ", response.status_code)
    print("Response: ", expense)


def add_new_expense() -> None:
    new_expense = {}
    
    print("Please enter a name for the expense: ", end='')
    name = input().strip()
    new_expense["name"] = name
    print("Please enter an amount for the expense: ", end='')
    amount = float(input().strip())
    new_expense["amount"] = amount
    print("Please enter a category for the expense: ", end='')
    category = input().strip()
    new_expense["category"] = category
    print("Please enter a date for the expense: ", end='')
    date = input().strip()
    new_expense["date"] = date 

    response = requests.post(base_url + "/expenses", json=new_expense)
    print("Status code: ", response.status_code)
    print("Response: ", response.json())

    
def update_existing_expense() -> None:
    update = {}
    cont = True
    print("Please enter the expense id you wish to update: ", end='')
    expense_id = input().strip()
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

                if choice == 1:
                    print("Enter a new name: ", end='')
                    name = input().strip()
                    update["name"] = name
                elif choice == 2:
                    print("Enter a new amount: ", end='')
                    amount = float(input().strip())
                    update["amount"] = amount
                elif choice == 3:
                    print("Enter a new category: ", end='')
                    category = input().strip()
                    update["category"] = category
                elif choice == 4:
                    print("Enter a new date: ", end='')
                    date = input().strip()
                    update["date"] = date
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
    print("Please enter the expense id you wish to replace: ", end='')
    expense_id = input().strip()
    
    print("Please enter a name for the expense: ", end='')
    name = input().strip()
    replacement_expense["name"] = name
    print("Please enter an amount for the expense: ", end='')
    amount = float(input().strip())
    replacement_expense["amount"] = amount
    print("Please enter a category for the expense: ", end='')
    category = input().strip()
    replacement_expense["category"] = category
    print("Please enter a date for the expense: ", end='')
    date = input().strip()
    replacement_expense["date"] = date 

    response = requests.put(base_url + f"/expenses/{expense_id}", json=replacement_expense)
    print("Status code: ", response.status_code)
    print("Response: ", response.json())


def delete_expense() -> None:
    print("Please enter the expense id you wish to delete: ", end='')
    expense_id = input().strip()

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