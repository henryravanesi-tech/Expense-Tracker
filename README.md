# Expense Tracker

The third version of a personal expense tracker. Built with FastAPI, SQLite, and a terminal client. The API lets users create, view, search, update, replace, and delete expenses, while SQLite keeps the data saved after the server stops.

## Features

- Add new expenses with a name, amount, category, and date
- View all expenses, or filter them by any combination of fields
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
| GET | `/expenses` with optional query parameters | Search expenses by name, category, amount range, and date range |
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

This is V3 of the project. Expenses are stored in a SQLite file, so the data is saved even after the server restarts.

In version 3, client output and input validation were improved. A search-by-filter feature was added, improving on the category-only search from the last version. To clean up the file structure, client helper functions were moved into their own file, and the Pydantic models were also moved into their own file.

The main goal of V3 was to improve client output, improve input validation, and add a better search feature that lets users filter by any combination of expense fields. The program now catches empty inputs, wrong data types, and inputs outside of the valid range. It also returns clear messages for backend errors and empty results.

## Future Improvements

- Add summary endpoints for total spending, spending by category, and spending by date range
- Add a simple frontend for interacting with the API in a browser
