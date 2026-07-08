# Expense Tracker
The second version of a personal expense tracker. Built with FastAPI, SQLite, and a terminal client. The API lets users create, view, filter, update, replace, and delete expenses, while SQLite keeps the data saved after the server stops.

## Features

- Add new expenses with a name, amount, category, and date
- View all expenses, or filter them by category
- Look up a single expense by its ID
- Update one or more fields of an existing expense
- Fully replace an existing expense
- Delete an expense
- Store expenses in a SQLite database
- Validate empty inputs, positive amounts, and date formatting

## Tech Stack

- **Python** – main language
- **FastAPI** – the web framework for the API
- **Uvicorn** – the server that runs the API
- **Pydantic** – validates the expense data
- **Requests** – used by the terminal client to call the API
- **SQLite** – stores expenses in a local database file


## API Routes

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Check that the API is running |
| GET | `/expenses` | View all expenses |
| GET | `/expenses?category={category}` | View expenses filtered by category |
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
python -m venv .venv

# Mac/Linux
source .venv/bin/activate

# Windows 
.venv\Scripts\activate

pip install -r requirements.txt
```

## Usage

The project has two parts: the API server and the terminal client. Start the server first, then run the client in a second terminal.

**1. Start the API server:**

```bash
uvicorn main:app --reload
```

The API runs at `http://127.0.0.1:8000`. You can also open `http://127.0.0.1:8000/docs` in your browser to see FastAPI's documentation. The SQLite database file will be created automatically when the API starts.

**2. Start the terminal client:**

```bash
python client_terminal.py
```

Then follow the on-screen menu to add, view, update, and delete expenses.

## Notes

This is V2 of the project. Expenses are stored in a SQLite file, so the data is saved even after the server restarts.

The main goal of V2 was to replace in-memory storage with SQLite, so expenses are actually stored in a local database file and still exist after the server restarts. I also improved input validation so empty inputs, invalid numbers, and incorrectly formatted dates are rejected, and the user is asked to re-enter only the incorrect input.

## Future Improvements

- Add filtering by amount and date
- Support multiple filters at once, like category, date, and amount range
- Add summary endpoints for total spending, spending by category, and spending by date range
- Move Pydantic models into a separate `models.py` file
- Create helper functions for repeated terminal client input validation
- Improve terminal output formatting
- Eventually add a simple frontend for interacting with the API in a browser
