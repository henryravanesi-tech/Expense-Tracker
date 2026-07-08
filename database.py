import sqlite3

db_name = "expenses.db"

def get_connection():

    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row
    return conn

def create_table():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            name TEXT NOT NULL,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            date TEXT NOT NULL       
        )
    """)

    conn.commit()
    conn.close()


def get_all_expenses():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
    "SELECT * FROM expenses"
    )

    rows = cursor.fetchall()
    conn.close()

    return [dict(row) for row in rows]


def get_expense(expense_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
    "SELECT * FROM expenses WHERE id = ?", 
    (expense_id,)
    )

    row = cursor.fetchone()
    conn.close()

    if row is None:
        return None
    
    return dict(row)


def get_expense_cat(category):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
    "SELECT * FROM expenses WHERE category = ?",
    (category,)
    )

    rows = cursor.fetchall()
    conn.close()

    return [dict(row) for row in rows]


def create_expense(name, amount, category, date_entered):

    conn = get_connection()
    cursor = conn.cursor()
    txt_date = date_entered.isoformat()

    cursor.execute(
    """
    INSERT INTO expenses (name, amount, category, date)
    VALUES (?, ?, ?, ?)
    """,
    (name, amount, category, txt_date)
    )

    new_id = cursor.lastrowid
    
    conn.commit()
    conn.close()

    return new_id


def modify_expense(expense_id, name=None, amount=None, category=None, date_entered=None):

    conn = get_connection()
    cursor = conn.cursor()

    fields = []
    values = []

    if name is not None:
        fields.append("name = ?")
        values.append(name)

    if amount is not None: 
        fields.append("amount = ?")
        values.append(amount)

    if category is not None:
        fields.append("category = ?")
        values.append(category)

    if date_entered is not None:
        txt_date = date_entered.isoformat()
        fields.append("date = ?")
        values.append(txt_date)

    if len(fields) == 0:
        conn.close()
        return False
    
    values.append(expense_id)

    sql =  f"UPDATE expenses SET {', '.join(fields)} WHERE id = ?"

    cursor.execute(sql, values)

    rows_changed = cursor.rowcount

    conn.commit()
    conn.close()

    return rows_changed > 0


def replace_expense(expense_id, name, amount, category, date_entered):

    conn = get_connection()
    cursor = conn.cursor()
    txt_date = date_entered.isoformat()
    cursor.execute(
    "UPDATE expenses SET name = ?, amount = ?, category = ?, date = ? WHERE id = ?", (name, amount, category, txt_date, expense_id)
    )

    rows_changed = cursor.rowcount

    conn.commit()
    conn.close()
    
    return rows_changed > 0


def delete_expense(expense_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
    "DELETE FROM expenses WHERE id = ?", (expense_id,)
    )

    rows_changed = cursor.rowcount

    conn.commit()
    conn.close()

    return rows_changed > 0