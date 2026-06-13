from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()
expenses = {
    1: {"name": "Chipotle", "amount": 12.5, "category": "food", "date": "2026-06-08"},
    2: {"name": "Coffee", "amount": 4.5, "category": "drink", "date": "2026-06-08"},
    3: {"name": "Chick-fil-A", "amount": 15.5, "category": "food", "date": "2026-06-08"}
}
next_id = 4


class Expense(BaseModel):
    name: str
    amount: float
    category: str
    date: str

class Expense_Update(BaseModel):
    name: str | None = None 
    amount: float | None = None
    category: str | None = None 
    date: str | None = None
    


@app.get("/")
def home():
    return {"message": "the tracker is up and running"}

@app.get("/expenses")
def get_expenses(category: str | None = None):
    if category is None:
        return expenses
    else:
        cat_expenses = {}
        for expense_id, expense in expenses.items():
            if expense["category"] == category:
                cat_expenses[expense_id] = expense
        return cat_expenses

@app.get("/expenses/{expense_id}")
def grab_expense(expense_id: int):
    if expense_id in expenses:
        return expenses[expense_id]
    else:
        raise HTTPException(status_code=404, detail="expense not found")


@app.post("/expenses", status_code=201)
def new_expense(expense: Expense):
    global next_id

    clean_expense = expense.model_dump()
    expenses[next_id] = clean_expense
    next_id += 1
    return {"message": "expense saved successfully", "expense": clean_expense}

    
@app.patch("/expenses/{expense_id}")
def update_expense(expense_id: int, expense: Expense_Update):
    
    if expense_id in expenses:
        
        empty_check = expense.model_dump(exclude_none=True)
        if empty_check == {}:
            raise HTTPException(status_code=400, detail="no update fields provided")
    
        if expense.name is not None:
            expenses[expense_id]["name"] = expense.name
        if expense.amount is not None:
            expenses[expense_id]["amount"] = expense.amount
        if expense.category is not None:
            expenses[expense_id]["category"] = expense.category
        if expense.date is not None:
            expenses[expense_id]["date"] = expense.date
        
        return {"message": "expense updated successfully", "expense": expenses[expense_id]}
            
    else:
        raise HTTPException(status_code=404, detail="expense not found")
    

@app.put("/expenses/{expense_id}")
def replace_expense(expense_id: int, expense: Expense):
    if expense_id in expenses:
        clean_expense = expense.model_dump()
        expenses[expense_id] = clean_expense
        return  {"message": "expense updated successfully", "expense": clean_expense}
    else:
        raise HTTPException(status_code=404, detail="expense not found")


@app.delete("/expenses/{expense_id}")
def delete_expense(expense_id: int):
    if expense_id in expenses:
        deleted = expenses.pop(expense_id, None)
        return {"message": "expense deleted successfully", "deleted expense": deleted}
    else:
        raise HTTPException(status_code=404, detail="expense not found")