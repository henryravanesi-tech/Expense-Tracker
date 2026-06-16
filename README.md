# Expense Tracker
A simple personal expense tracker built with FastAPI and an interactive client. The API supports adding, viewing, filtering, updating, replacing, and deleting expenses. The terminal client lets users interact with the API without manually writing HTTP requests.

## Features

- Add new expenses with a name, amount, category, and date
- View all expenses, or filter them by category
- Look up a single expense by its ID
- Update one or more fields of an existing expense
- Fully replace an existing expense
- Delete an expense

## Tech Stack

- **Python** – main language
- **FastAPI** – the web framework for the API
- **Uvicorn** – the server that runs the API
- **Pydantic** – validates the expense data
- **Requests** – used by the terminal client to call the API


## API Routes

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Check that the API is running |
| GET | `/expenses` | View all expenses |
| GET | `/expenses?category=food` | Filter expenses by category |
| GET | `/expenses/{expense_id}` | View one expense by ID |
| POST | `/expenses` | Add a new expense |
| PATCH | `/expenses/{expense_id}` | Update one or more fields of an expense |
| PUT | `/expenses/{expense_id}` | Fully replace an expense |
| DELETE | `/expenses/{expense_id}` | Delete an expense |

## Setup

Get the project onto your machine and install what it needs. You only do this once.

```bash
git clone https://github.com/henryravanesi-tech/Expense-Tracker.git
cd Expense-Tracker

# (optional) create and activate a virtual environment
python -m venv venv

# Mac/Linux
source venv/bin/activate

# Windows 
venv\Scripts\activate

pip install -r requirements.txt
```

## Usage

The project has two parts: the API server and the terminal client. Start the server first, then run the client in a second terminal.

**1. Start the API server:**

```bash
uvicorn main:app --reload
```

The API runs at `http://127.0.0.1:8000`. You can also open `http://127.0.0.1:8000/docs` in your browser to see FastAPI's documentation.

**2. Start the terminal client:**

```bash
python client_terminal.py
```

Then follow the on-screen menu to add, view, update, and delete expenses.

## Notes

This is V1 of the project. Expenses are stored in memory, so the data resets when the server restarts.

The goal of V1 was to practice FastAPI routes, JSON request/response, status codes, and building a terminal client that communicates with the API through HTTP requests.

## Plans for V2

- Move expense storage from an in-memory dictionary to SQLite
- Keep expenses saved after the server restarts
- Improve terminal output formatting
- Add better input validation in the terminal client
- Start separating backend, database, and client logic into cleaner files
