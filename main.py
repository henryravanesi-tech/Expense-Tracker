from fastapi import FastAPI, HTTPException
from database import search_expenses, create_table, get_expense, create_expense, modify_expense, replace_expense, delete_expense
from models import Expense, Expense_Update


app = FastAPI()

create_table()


@app.get("/")
def home():
    return {"message": "The tracker is up and running."}

@app.get("/expenses")
def get_expenses(name: str | None = None, category: str | None = None, min_amount: float | None = None, max_amount: float | None = None, start_date: str | None = None, end_date: str | None = None):
    return search_expenses(name=name, category=category, min_amount=min_amount, max_amount=max_amount, start_date=start_date, end_date=end_date)

@app.get("/expenses/{expense_id}")
def grab_expense(expense_id: int):
    expense = get_expense(expense_id)
    if expense is None:
        raise HTTPException(status_code=404, detail="Expense not found.")
    return expense


@app.post("/expenses", status_code=201)
def new_expense(expense: Expense):

    new_id = create_expense(expense.name, expense.amount, expense.category, expense.date)

    return {"message": "Expense saved successfully.", "expense": get_expense(new_id)}

    
@app.patch("/expenses/{expense_id}")
def update_expense(expense_id: int, expense: Expense_Update):

    if expense.name is None and expense.amount is None and expense.category is None and expense.date is None:
        raise HTTPException(status_code=400, detail="No update fields provided.")
    
    update = modify_expense(expense_id, name=expense.name, amount=expense.amount, category=expense.category, date_entered=expense.date)

    if update is False:
        raise HTTPException(status_code=404, detail="Expense not found.")
    
    return {"message": "Expense updated successfully.", "expense": get_expense(expense_id)}   
    

@app.put("/expenses/{expense_id}")
def swap_expense(expense_id: int, expense: Expense):
    
    replace = replace_expense(expense_id, name=expense.name, amount=expense.amount, category=expense.category, date_entered=expense.date)

    if replace is False:
        raise HTTPException(status_code=404, detail="Expense not found.")
        
    return  {"message": "Expense updated successfully.", "expense": get_expense(expense_id)}


@app.delete("/expenses/{expense_id}")
def remove_expense(expense_id: int):

    expense_deleted = get_expense(expense_id)

    remove = delete_expense(expense_id)

    if remove is False:
        raise HTTPException(status_code=404, detail="Expense not found.")
    
    return {"message": "Expense deleted successfully.", "expense": expense_deleted}