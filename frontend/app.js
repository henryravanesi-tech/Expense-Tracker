const API_URL = "http://127.0.0.1:8000";

let currentQuery = "";
let editingId = null;


// our own errors (400/404) come back as a string, but FastAPI's
// validation errors (422) come back as a list, so handle both
function errorMessage(detail, fallback) {

    if (typeof detail === "string") {

        return detail;

    }

    if (Array.isArray(detail) && detail.length > 0) {

        return detail.map(function(item) {

            return item.msg;

        }).join("; ");

    }

    return fallback;

}


function refresh() {

    loadExpenses(currentQuery);

    loadSummary(currentQuery);

}



// load expenses

async function loadExpenses(query = "") {

    try {

        const response = await fetch(
            API_URL + "/expenses" + (query ? `?${query}` : "")
        );


        if (!response.ok) {

            throw new Error("Could not load expenses.");

        }


        const expenses = await response.json();


        displayExpenses(expenses);


    } catch (error) {

        console.log(error);

    }

}



// show the expense rows

function displayExpenses(expenses) {

    const expenseList =
        document.getElementById("expense-list");


    expenseList.innerHTML = "";


    if (expenses.length === 0) {

        const emptyMessage =
            document.createElement("p");


        emptyMessage.classList.add("empty-message");

        emptyMessage.textContent =
            "No expenses found.";


        expenseList.appendChild(emptyMessage);


        return;

    }



    for (const expense of expenses) {


        const row =
            document.createElement("div");


        row.classList.add("expense-item");



        const id =
            document.createElement("span");

        id.textContent = expense.id;



        const name =
            document.createElement("span");

        name.textContent = expense.name;



        const category =
            document.createElement("span");

        category.textContent = expense.category;



        const date =
            document.createElement("span");

        date.textContent = expense.date;



        const amount =
            document.createElement("span");

        amount.textContent =
            `$${expense.amount.toFixed(2)}`;



        const actions =
            document.createElement("div");


        actions.classList.add("expense-actions");



        const editButton =
            document.createElement("button");


        editButton.textContent =
            "Edit";


        editButton.classList.add("edit-button");

        editButton.type = "button";



        editButton.addEventListener(
            "click",
            function() {

                startEdit(expense);

            }
        );



        const deleteButton =
            document.createElement("button");


        deleteButton.textContent =
            "Delete";


        deleteButton.classList.add("delete-button");

        deleteButton.type = "button";



        deleteButton.addEventListener(
            "click",
            function() {

                deleteExpense(expense.id);

            }
        );



        actions.appendChild(editButton);

        actions.appendChild(deleteButton);



        row.appendChild(id);

        row.appendChild(name);

        row.appendChild(category);

        row.appendChild(date);

        row.appendChild(amount);

        row.appendChild(actions);



        expenseList.appendChild(row);

    }

}



// load the total

async function loadSummary(query = "") {

    try {

        const response = await fetch(
            API_URL + "/expenses/summary" + (query ? `?${query}` : "")
        );


        if (!response.ok) {

            throw new Error("Could not load summary.");

        }


        const summary =
            await response.json();



        document
            .getElementById("total-spending")
            .textContent =
            `$${summary.total.toFixed(2)}`;



        document
            .getElementById("expense-count")
            .textContent =
            `${summary.expense_count} expenses`;


    } catch (error) {

        console.log(error);

    }

}



// filters

const filterButton =
    document.getElementById("filter-button");



filterButton.addEventListener(
    "click",
    function() {


        const name =
            document
                .getElementById("filter-name")
                .value
                .trim();



        const category =
            document
                .getElementById("filter-category")
                .value
                .trim();



        const minAmount =
            document
                .getElementById("filter-min")
                .value;



        const maxAmount =
            document
                .getElementById("filter-max")
                .value;



        const startDate =
            document
                .getElementById("filter-start")
                .value;



        const endDate =
            document
                .getElementById("filter-end")
                .value;



        if (minAmount && maxAmount && Number(minAmount) > Number(maxAmount)) {

            alert("Minimum amount can't be greater than maximum amount.");

            return;

        }



        if (startDate && endDate && startDate > endDate) {

            alert("Start date can't be after end date.");

            return;

        }



        const params =
            new URLSearchParams();



        if (name) {

            params.append(
                "name",
                name
            );

        }



        if (category) {

            params.append(
                "category",
                category
            );

        }



        if (minAmount) {

            params.append(
                "min_amount",
                minAmount
            );

        }



        if (maxAmount) {

            params.append(
                "max_amount",
                maxAmount
            );

        }



        if (startDate) {

            params.append(
                "start_date",
                startDate
            );

        }



        if (endDate) {

            params.append(
                "end_date",
                endDate
            );

        }



        currentQuery =
            params.toString();



        refresh();

    }
);



// find by id

const searchIdButton =
    document.getElementById("search-id-button");



searchIdButton.addEventListener(
    "click",
    searchById
);



async function searchById() {

    document.getElementById("search-message").textContent = "";

    const expenseId =
        document
            .getElementById("search-id")
            .value;



    if (!expenseId || Number(expenseId) < 1) {

        alert("Please enter a valid expense ID.");

        return;

    }



    try {


        const response = await fetch(
            API_URL + `/expenses/${expenseId}`
        );



        const result =
            await response.json();



        if (!response.ok) {

            document.getElementById("search-message").textContent =
                errorMessage(result.detail, "Expense not found.");

            return;

        }



        displayExpenses([result]);



        document
            .getElementById("total-spending")
            .textContent =
            `$${result.amount.toFixed(2)}`;



        document
            .getElementById("expense-count")
            .textContent =
            "1 expense";


    } catch (error) {


        console.log(error);


        alert(
            "Could not connect to the API."
        );

    }

}



// show all

const showAllButton =
    document.getElementById("show-all-button");



showAllButton.addEventListener(
    "click",
    function() {

        document.getElementById("search-message").textContent = "";

        document.getElementById("search-id").value = "";

        document.getElementById("filter-name").value = "";

        document.getElementById("filter-category").value = "";

        document.getElementById("filter-min").value = "";

        document.getElementById("filter-max").value = "";

        document.getElementById("filter-start").value = "";

        document.getElementById("filter-end").value = "";



        currentQuery = "";



        refresh();

    }
);



// add/edit form

const addExpenseButton =
    document.getElementById("add-expense-button");


const addExpenseForm =
    document.getElementById("add-expense-form");


const cancelAddButton =
    document.getElementById("cancel-add-button");


const saveExpenseButton =
    document.getElementById("save-expense-button");


const formTitle =
    document.getElementById("form-title");



function clearForm() {

    document.getElementById("add-name").value = "";

    document.getElementById("add-amount").value = "";

    document.getElementById("add-category").value = "";

    document.getElementById("add-date").value = "";

    document.getElementById("add-message").textContent = "";

}



function openAddForm() {

    editingId = null;

    formTitle.textContent = "Add Expense";

    saveExpenseButton.textContent = "Save Expense";

    clearForm();

    addExpenseForm.classList.remove("hidden");

}



function startEdit(expense) {

    editingId = expense.id;

    formTitle.textContent = `Edit Expense #${expense.id}`;

    saveExpenseButton.textContent = "Save Changes";

    document.getElementById("add-name").value = expense.name;

    document.getElementById("add-amount").value = expense.amount;

    document.getElementById("add-category").value = expense.category;

    document.getElementById("add-date").value = expense.date;

    document.getElementById("add-message").textContent = "";

    addExpenseForm.classList.remove("hidden");

    addExpenseForm.scrollIntoView({ behavior: "smooth" });

}



function closeForm() {

    addExpenseForm.classList.add("hidden");

    editingId = null;

    clearForm();

}



addExpenseButton.addEventListener(
    "click",
    openAddForm
);



cancelAddButton.addEventListener(
    "click",
    closeForm
);



saveExpenseButton.addEventListener(
    "click",
    saveExpense
);



// save (post when adding, put when editing)

async function saveExpense() {


    const name =
        document
            .getElementById("add-name")
            .value
            .trim();



    const amount =
        document
            .getElementById("add-amount")
            .value;



    const category =
        document
            .getElementById("add-category")
            .value
            .trim();



    const date =
        document
            .getElementById("add-date")
            .value;



    const message =
        document.getElementById("add-message");



    if (!name || !amount || !category || !date) {

        message.textContent =
            "Please fill out every field.";

        return;

    }



    if (Number(amount) <= 0) {

        message.textContent =
            "Amount must be greater than 0.";

        return;

    }



    const expense = {

        name: name,

        amount: Number(amount),

        category: category,

        date: date

    };



    const isEditing = editingId !== null;


    const url = isEditing
        ? API_URL + `/expenses/${editingId}`
        : API_URL + "/expenses";



    try {


        const response = await fetch(
            url,
            {

                method: isEditing ? "PUT" : "POST",


                headers: {

                    "Content-Type": "application/json"

                },


                body: JSON.stringify(expense)

            }
        );



        const result =
            await response.json();



        if (!response.ok) {

            message.textContent =
                errorMessage(result.detail, "Could not save expense.");

            return;

        }



        message.textContent =
            isEditing
                ? "Expense updated successfully."
                : "Expense added successfully.";



        refresh();



        setTimeout(
            closeForm,
            700
        );


    } catch (error) {


        console.log(error);


        message.textContent =
            "Could not connect to the API.";

    }

}



// delete

async function deleteExpense(expenseId) {


    const confirmed =
        confirm(
            "Are you sure you want to delete this expense?"
        );



    if (!confirmed) {

        return;

    }



    try {


        const response = await fetch(
            API_URL + `/expenses/${expenseId}`,
            {

                method: "DELETE"

            }
        );



        if (!response.ok) {


            const result =
                await response.json();


            alert(
                errorMessage(result.detail, "Could not delete expense.")
            );


            return;

        }



        refresh();


    } catch (error) {


        console.log(error);


        alert(
            "Could not connect to the API."
        );

    }

}



// first load

refresh();