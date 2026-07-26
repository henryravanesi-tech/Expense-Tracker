import requests
from client_helpers import get_expense_id, get_category, get_name, get_amount, get_date, get_min_amount, get_max_amount, get_start_date, get_end_date

base_url = "http://127.0.0.1:8000"

def print_expense(expense):
    print(f"[{expense['id']}] {expense['name']} - ${expense['amount']:.2f} - {expense['category']} - {expense['date']}")

def print_expenses(expenses):
    if len(expenses) == 0:
        print("No expenses found.")
        return 
    else:
        print(f"Found {len(expenses)} expenses.")
        for expense in expenses:
            print(f"[{expense['id']}] {expense['name']} - ${expense['amount']:.2f} - {expense['category']} - {expense['date']}")

def print_update(expense):
    print("Expense updated successfully.")
    print(f"[{expense['id']}] {expense['name']} - ${expense['amount']:.2f} - {expense['category']} - {expense['date']}")

def print_added(expense):
    print("Expense added successfully.")
    print(f"[{expense['id']}] {expense['name']} - ${expense['amount']:.2f} - {expense['category']} - {expense['date']}")

def print_deleted(expense):
    print("Expense deleted successfully.")
    print(f"[{expense['id']}] {expense['name']} - ${expense['amount']:.2f} - {expense['category']} - {expense['date']}")
def menu() -> int:
    
    print("1. Check API status")
    print("2. View all expenses")
    print("3. Search expenses by filter")
    print("4. Get an expense by ID")
    print("5. Add a new expense")
    print("6. Modify/update a part of an expense")
    print("7. Fully replace a specific expense")
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
    
    print_expenses(expenses)


def search_expenses() -> None:
    cont = True 
    params = {}
    
    while cont:
        try:
            print("Select filters to apply, continue will send through the request.")
            print("1. name")
            print("2. amount")
            print("3. category")
            print("4. date")
            print("5. continue")
            choice = int(input().strip())
            if choice >= 1 and choice <= 5:
                if choice == 1:
                    params["name"] = get_name()
            
                elif choice == 2:
                    amount_l = True 
                    while amount_l:
                        params["min_amount"] = get_min_amount()
                        params["max_amount"] = get_max_amount()
                        if params["min_amount"] <= params["max_amount"]:
                            amount_l = False
                        else:
                            print("Minimum amount can't be greater than maximum amount, please try again.")

                    

                elif choice == 3:
                    params["category"] = get_category()

                elif choice == 4:
                    date_l = True 
                    while date_l:
                        params["start_date"] = get_start_date()
                        params["end_date"] = get_end_date()
                        if params["start_date"] <= params["end_date"]:
                            date_l = False
                        else:
                            print("start date can't be after end date, please try again.")

                elif choice == 5:
                    cont = False

            else:
                raise ValueError
                
        except ValueError:
                print("Invalid input, please try again.")        
    

    response = requests.get(base_url + "/expenses", params=params)
    search_res = response.json()
    print_expenses(search_res)


def get_specific_expense() -> None:
    
    expense_id = get_expense_id()
    
    response = requests.get(base_url + f"/expenses/{expense_id}")
    expense = response.json()

    if response.status_code >= 400:
        print("Error:", expense["detail"])
        return 

    print_expense(expense)


def add_new_expense() -> None:
    new_expense = {}

    new_expense["name"] = get_name()

    new_expense["amount"] = get_amount()

    new_expense["category"] = get_category()

    new_expense["date"] = get_date()

    response = requests.post(base_url + "/expenses", json=new_expense)
    added = response.json()
    if response.status_code >= 400:
        print("Error:", added["detail"])
        return
    print_added(added["expense"])
    

def update_existing_expense() -> None:
    update = {}
    cont = True

    expense_id = get_expense_id()

    print("Select which fields to update, continue will send through the request.")
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
                    update["name"] = get_name()
        
                elif choice == 2:
                    update["amount"] = get_amount()

                elif choice == 3:
                    update["category"] = get_category()

                elif choice == 4:
                    update["date"] = get_date()

                elif choice == 5:
                    cont = False

            else:
                raise ValueError
            
        except ValueError:
            print("Invalid input, please try again.")
    
    response = requests.patch(base_url + f"/expenses/{expense_id}", json=update)
    updated = response.json()

    if response.status_code >= 400:
        print("Error:", updated["detail"])
        return 
    
    print_update(updated["expense"])

        
def replace_expense() -> None:
    replacement_expense = {}
    
    expense_id = get_expense_id()
    
    replacement_expense["name"] = get_name()

    replacement_expense["amount"] = get_amount()

    replacement_expense["category"] = get_category()

    replacement_expense["date"] = get_date()

    response = requests.put(base_url + f"/expenses/{expense_id}", json=replacement_expense)
    replaced = response.json()

    if response.status_code >= 400:
        print("Error:", replaced["detail"])
        return 
    
    print_update(replaced["expense"])


def delete_expense() -> None:

    expense_id = get_expense_id()

    response = requests.delete(base_url + f"/expenses/{expense_id}")
    deleted = response.json()

    if response.status_code >= 400:
        print("Error:", deleted["detail"])
        return 
    
    print_deleted(deleted["expense"])



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
            search_expenses()
        
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
            print("Program closed.")


if __name__ == "__main__":
    main()