
````markdown
# 🛒 E-Commerce Order Explorer

A beginner-friendly **SQL + PostgreSQL + Python + Streamlit** project designed to practice real-world SQL querying through an interactive web interface.

The project provides a simple Streamlit application where users can:

- Create and connect to a PostgreSQL database
- Automatically create the `orders` table
- Insert e-commerce order data through an interactive form
- Validate customer and city inputs
- Execute custom SQL queries through a SQL editor
- View query results in a structured Pandas DataFrame
- Practice SQL concepts such as `SELECT`, `WHERE`, `ORDER BY`, and `LIMIT`

This project was built as **Project 1 of a structured SQL/Data Engineering learning roadmap**.

---

## 📌 Project Overview

The **E-Commerce Order Explorer** simulates a small e-commerce order management and analysis system.

Instead of working only inside a database client, this project adds a simple **Streamlit web interface** on top of PostgreSQL.

The application allows the user to switch between two main operations:

1. **Insert Data**
2. **Fetch Data**

This makes the project useful not only for learning SQL but also for understanding how Python applications interact with relational databases.

---

## 🎯 Project Objectives

The main objectives of this project are:

- Understand the fundamentals of SQL querying
- Practice PostgreSQL database operations
- Connect Python applications with PostgreSQL
- Build a simple interactive UI using Streamlit
- Insert structured data into a relational database
- Validate user input before database insertion
- Execute SQL queries dynamically
- Display database results in a user-friendly table
- Develop the habit of translating business requirements into SQL queries
- Understand the basic flow of a database-driven application

---

## 🧰 Technologies Used

| Technology | Purpose |
|---|---|
| **Python** | Application logic |
| **PostgreSQL** | Relational database |
| **psycopg2** | PostgreSQL database connectivity |
| **Streamlit** | Interactive web UI |
| **Pandas** | Formatting and displaying query results |
| **python-dotenv** | Environment variable management |
| **pgAdmin 4** | PostgreSQL database management and SQL testing |
| **Git/GitHub** | Version control and project documentation |

---

# 🏗️ Application Architecture

The project follows a simple modular architecture:

```text
                    ┌─────────────────────────┐
                    │      Streamlit UI       │
                    │  E-Commerce Order       │
                    │       Explorer          │
                    └────────────┬────────────┘
                                 │
                    ┌────────────▼────────────┐
                    │      Python Logic       │
                    │                         │
                    │  Data Insertion         │
                    │  Query Execution        │
                    │  Validation              │
                    └────────────┬────────────┘
                                 │
                         ┌───────▼────────┐
                         │    psycopg2    │
                         │ PostgreSQL API │
                         └───────┬────────┘
                                 │
                    ┌────────────▼────────────┐
                    │      PostgreSQL         │
                    │   ecommerce_training    │
                    │                         │
                    │        orders           │
                    └────────────┬────────────┘
                                 │
                    ┌────────────▼────────────┐
                    │       Query Result      │
                    │                         │
                    │       Pandas DataFrame  │
                    └─────────────────────────┘
````

---

# 🖥️ Streamlit User Interface

The project includes an interactive Streamlit interface called:

> **E-Commerce Order Explorer**

The application provides a simple menu:

```text
What Do You Want?

├── Insert Data
└── Fetch Data
```

---

## ➕ Insert Data Interface

The **Insert Data** section provides an interactive form for entering new orders.

The form includes:

* Order ID
* Customer Name
* City Name
* Order Date
* Total Amount
* Order Status
* INSERT button

### Available Order Statuses

```text
Pending
Shipped
Delivered
Cancelled
```

The user does not need to manually write an `INSERT` statement.

Instead, the Streamlit form collects the information and the Python application sends the data to PostgreSQL.

### Example

```text
Enter Order ID
1001

Enter Customer Name
Ali Raza

Enter City Name
Faisalabad

Enter Order Date
2026/01/05

Enter Total Amount
7800

Select Order Status
Shipped

[ INSERT ]
```

---

# ✅ Input Validation

Before inserting data into PostgreSQL, the application performs basic validation.

### Customer Name Validation

The application:

* Removes unnecessary whitespace
* Converts the name into title case
* Prevents empty names
* Prevents names containing invalid characters

Example:

```text
ali raza
```

is normalized to:

```text
Ali Raza
```

The application also checks that the name contains alphabetic characters.

---

### City Validation

The city input is similarly:

* Stripped of unnecessary whitespace
* Converted to title case
* Checked for empty values
* Checked for invalid characters

Example:

```text
faisalabad
```

becomes:

```text
Faisalabad
```

---

# 🔎 Fetch Data Interface

The **Fetch Data** section provides a SQL query editor.

The user can write a PostgreSQL query directly in the Streamlit interface.

Example:

```sql
SELECT * FROM orders;
```

The interface provides:

```text
Write Your Query Here

[ SQL Query Editor ]

[ Run ]
```

After execution, the application retrieves the result from PostgreSQL and displays it as a Pandas DataFrame.

---

## 📊 Query Result Display

For queries that return rows, such as `SELECT` queries, the application:

1. Executes the SQL query
2. Retrieves the returned rows
3. Retrieves column names from the cursor metadata
4. Creates a Pandas DataFrame
5. Displays the DataFrame using Streamlit

Conceptually:

```text
SQL Query
    ↓
PostgreSQL
    ↓
Returned Rows
    ↓
Pandas DataFrame
    ↓
Streamlit Table
```

This provides a much cleaner way to inspect SQL query results than printing raw tuples.

---

# 🗄️ Database Design

The project uses a PostgreSQL database named:

```text
ecommerce_training
```

The primary table is:

```text
orders
```

---

## 📋 Orders Table

| Column          | Data Type     | Description             |
| --------------- | ------------- | ----------------------- |
| `order_id`      | INT           | Unique order identifier |
| `customer_name` | VARCHAR(100)  | Customer's name         |
| `city`          | VARCHAR(50)   | Customer/order city     |
| `order_date`    | DATE          | Date of the order       |
| `total_amount`  | NUMERIC(10,2) | Total order value       |
| `status`        | VARCHAR(20)   | Current order status    |

### Primary Key

```text
order_id
```

is used as the primary key to uniquely identify each order.

---

# 🏗️ Database Initialization

The application contains a database initialization process.

The project can:

1. Connect to PostgreSQL
2. Create the `ecommerce_training` database
3. Connect to the database
4. Create the `orders` table if it does not already exist

The table creation uses:

```sql
CREATE TABLE IF NOT EXISTS orders (
    order_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    city VARCHAR(50),
    order_date DATE,
    total_amount NUMERIC(10,2),
    status VARCHAR(20)
);
```

Using `IF NOT EXISTS` prevents the application from failing simply because the table already exists.

---

# 🔐 Environment Variables

Database credentials are not hard-coded directly into the application.

The project uses `python-dotenv` to load database configuration from environment variables.

Example `.env` structure:

```env
HOST=localhost
USER=your_postgres_username
PASSWORD=your_postgres_password
PORT=5432
DBNAME=ecommerce_training
```

> **Important:** Never commit your actual `.env` file or database password to GitHub.

Add the following to `.gitignore`:

```gitignore
.env
__pycache__/
.venv/
```

---

# 📁 Project Structure

The application is divided into multiple Python modules instead of putting everything into one file.

```text
E-Commerce Order Explorer/
│
├── main.py
├── connection.py
├── database.py
├── create_table.py
├── data_insertion.py
├── query.py
│
├── .env
├── .gitignore
└── README.md
```

---

## 📄 File Responsibilities

### `main.py`

Acts as the main Streamlit application.

Responsibilities:

* Configure the Streamlit interface
* Display the application title
* Show database connection status
* Create the database/table
* Display the Insert/Fetch selection
* Route the user to the appropriate functionality

---

### `connection.py`

Contains the reusable PostgreSQL connection function.

Main responsibility:

```text
Python Application
        ↓
get_connection()
        ↓
PostgreSQL
```

The database credentials are loaded from environment variables.

---

### `database.py`

Handles database initialization.

Responsibilities:

* Connect to PostgreSQL server
* Create the `ecommerce_training` database
* Handle connection errors
* Close the database connection

---

### `create_table.py`

Responsible for creating the `orders` table.

It uses:

```sql
CREATE TABLE IF NOT EXISTS
```

so the table does not need to be manually recreated every time the application runs.

---

### `data_insertion.py`

Responsible for the Streamlit data-entry interface.

Responsibilities:

* Collect order information
* Validate customer name
* Validate city
* Normalize user input
* Execute the `INSERT` query
* Display success/error messages

---

### `query.py`

Responsible for executing user-provided SQL queries.

Responsibilities:

* Provide the SQL editor
* Execute the query
* Detect whether the query returns rows
* Retrieve column names
* Convert results into a Pandas DataFrame
* Display results in Streamlit
* Display errors when query execution fails

---

# 🔄 Application Workflow

## Application Startup

```text
Run Streamlit Application
          ↓
      main.py
          ↓
Connect to PostgreSQL
          ↓
Create Database
          ↓
Create orders Table
          ↓
Display Streamlit UI
```

---

## Insert Workflow

```text
User selects "Insert Data"
          ↓
Streamlit displays form
          ↓
User enters order information
          ↓
Input validation
          ↓
Data normalization
          ↓
INSERT SQL statement
          ↓
PostgreSQL
          ↓
Success / Error message
```

---

## Fetch Workflow

```text
User selects "Fetch Data"
          ↓
SQL editor appears
          ↓
User writes SQL query
          ↓
Click "Run"
          ↓
PostgreSQL executes query
          ↓
Rows returned
          ↓
Pandas DataFrame
          ↓
Streamlit displays results
```

---

# 🧠 SQL Concepts Practiced

This project focuses on the fundamentals of SQL.

### 1. SELECT

Retrieving data from a table.

```sql
SELECT order_id, customer_name, total_amount
FROM orders;
```

---

### 2. WHERE

Filtering records.

```sql
SELECT *
FROM orders
WHERE status = 'Pending';
```

---

### 3. ORDER BY

Sorting query results.

```sql
SELECT *
FROM orders
ORDER BY total_amount DESC;
```

---

### 4. LIMIT

Restricting the number of returned records.

```sql
SELECT *
FROM orders
ORDER BY total_amount DESC
LIMIT 5;
```

---

### 5. Combining SQL Clauses

The project also practices combining:

```text
SELECT
   ↓
WHERE
   ↓
ORDER BY
   ↓
LIMIT
```

Example business requirement:

> Find the five highest-value pending orders.

This requires translating a business requirement into an appropriate SQL query.

---

# 📊 Business Questions Practiced

The project was designed around practical e-commerce questions such as:

### Basic Data Retrieval

* Retrieve all orders
* Retrieve selected columns
* View customer names
* View order amounts

### Filtering

* Find pending orders
* Find orders from Lahore
* Find high-value orders
* Find orders below a specific amount

### Sorting

* Sort orders by highest amount
* Sort orders by newest date
* Sort pending orders by date

### Top-N Analysis

* Find the top 5 highest-value orders
* Find the most recent orders
* Find the highest-value completed/delivered orders

These questions help develop the habit of converting a business requirement into SQL logic.

---

# 🧪 Query Testing & Verification

SQL queries were tested using PostgreSQL/pgAdmin as well as the Streamlit SQL interface.

Testing includes checking:

* Returned row count
* Correct columns
* Filtering behavior
* Sorting order
* `LIMIT` behavior
* Unexpected or empty results
* Invalid SQL queries
* Duplicate primary-key insertion
* Input validation errors

For example, if a query is expected to return the top five orders, the result should be verified to ensure:

```text
Number of returned rows = 5
```

and that the amounts are actually ordered from highest to lowest.

---

# ⚠️ Error Handling

The Python application includes basic exception handling around database operations.

If a database or SQL error occurs, the application displays an error message instead of silently failing.

Examples of possible errors include:

* Invalid SQL syntax
* Database connection failure
* Duplicate `order_id`
* Invalid database credentials
* Invalid table/column names
* Constraint violations

---

# 🔒 Security Considerations

The project follows some basic security practices:

* Database credentials are stored in `.env`
* Credentials are not hard-coded into source files
* `.env` should not be committed to GitHub
* Inserted form values are passed to `psycopg2` as query parameters

For example, the insertion operation uses parameterized values rather than manually constructing the SQL string with user input.

> **Note:** The Fetch Data interface intentionally allows users to enter SQL directly because this is a SQL-learning project. A production application should not expose unrestricted SQL execution to untrusted users.

---

# 🚀 Running the Project Locally

## 1. Clone the Repository

```bash
git clone <your-repository-url>
```

Move into the project directory:

```bash
cd E-Commerce-Order-Explorer
```

---

## 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install streamlit psycopg2-binary python-dotenv pandas
```

---

## 4. Configure Environment Variables

Create a `.env` file:

```env
HOST=localhost
USER=your_postgres_username
PASSWORD=your_postgres_password
PORT=5432
DBNAME=ecommerce_training
```

Update the values according to your PostgreSQL installation.

---

## 5. Start the Application

Run:

```bash
streamlit run main.py
```

Streamlit will start the local web application.

The application can then be opened in a browser through the local Streamlit address provided by the terminal.

---

# 🖥️ Development Environment

The project was developed and tested using:

* **Windows**
* **Visual Studio Code**
* **Python 3.12**
* **PostgreSQL**
* **pgAdmin 4**
* **Streamlit**

---

# 📈 What I Learned

Through this project, I practiced much more than writing basic SQL queries.

### SQL

* Writing `SELECT` queries
* Filtering using `WHERE`
* Sorting using `ORDER BY`
* Limiting results using `LIMIT`
* Combining multiple SQL clauses
* Translating business questions into SQL

### PostgreSQL

* Creating databases
* Creating tables
* Defining primary keys
* Working with PostgreSQL data types
* Executing queries
* Handling database constraints

### Python + PostgreSQL

* Establishing database connections
* Executing SQL from Python
* Using cursors
* Handling database exceptions
* Using environment variables
* Structuring database-related code into modules

### Streamlit

* Building interactive web interfaces
* Creating input forms
* Using text inputs
* Using number inputs
* Using date inputs
* Using select boxes
* Creating buttons
* Displaying success/error messages
* Displaying DataFrames
* Building a simple database application UI

### Data Engineering Mindset

The project also introduces an important Data Engineering pattern:

```text
Application
     ↓
Database
     ↓
SQL
     ↓
Structured Data
     ↓
Analysis
```

---

# 🧩 Why This Project Matters for Data Engineering

Although this is a beginner SQL project, it introduces concepts that are directly relevant to Data Engineering.

A typical Data Engineering workflow involves:

```text
Data Source
    ↓
Ingestion
    ↓
Database / Data Warehouse
    ↓
Transformation
    ↓
SQL
    ↓
Analytics
    ↓
Reporting / Applications
```

This project focuses on the database and SQL layer while also demonstrating how a Python application can interact with that layer.

The same concepts become increasingly important when working with:

* ETL pipelines
* ELT pipelines
* PostgreSQL
* Data warehouses
* Analytics engineering
* Apache Kafka
* Apache Spark
* PySpark
* Data transformation pipelines

---

# 🔮 Future Improvements

Possible improvements for future versions include:

* Add UPDATE functionality
* Add DELETE functionality
* Add dedicated search filters
* Add pagination
* Add SQL query history
* Add predefined SQL exercises
* Add query-result statistics
* Add charts and visual analytics
* Add authentication
* Add role-based access
* Add better database connection management
* Add logging
* Add automated tests
* Add Docker support
* Deploy the Streamlit application
* Add a production-safe query execution layer

---

# 🗺️ SQL Learning Roadmap

This project is **Project 1** in a progressive SQL learning series.

```text
Project 1
E-Commerce Order Explorer
        │
        ▼
SELECT / WHERE / ORDER BY / LIMIT
        │
        ▼
Project 2
Sales Filter & Investigation
        │
        ▼
AND / OR / IN / BETWEEN / LIKE
        │
        ▼
Project 3
Dirty Customer Data Cleanup
        │
        ▼
String / Number / Date / NULL Functions
        │
        ▼
Project 4
Order Classification Engine
        │
        ▼
CASE
        │
        ▼
Project 5
Sales Analytics Report
        │
        ▼
Aggregations / GROUP BY / HAVING
        │
        ▼
Project 6
E-Commerce Relational Analysis
        │
        ▼
JOINs
        │
        ▼
Project 7
Customer Ranking & Latest Records
        │
        ▼
Window Functions
        │
        ▼
Project 8
Maintainable SQL Transformation Layer
        │
        ▼
CTEs / Subqueries / Views / CTAS / Temp Tables
        │
        ▼
Project 9
SQL Data Engineering Capstone
```

---

# 📌 Project Status

**Status:** ✅ Completed

**Project:** 01

**Level:** Beginner

**Focus:** SQL Fundamentals + PostgreSQL + Python + Streamlit

---

# 👨‍💻 Skills Demonstrated

```text
SQL
PostgreSQL
Python
Streamlit
psycopg2
Pandas
Database Connectivity
Input Validation
Exception Handling
Environment Variables
Modular Python Architecture
Data Retrieval
Data Insertion
SQL Query Execution
Basic Data Engineering
```

---

# 💡 Key Takeaway

The main goal of this project was not simply to memorize SQL syntax.

The project was designed to build the ability to:

> **Understand a business requirement → translate it into SQL → execute it against PostgreSQL → verify the result → present the result through an application interface.**

The addition of a Streamlit interface makes the project closer to a small real-world database application rather than a collection of isolated SQL queries.

---

## ⭐ Project Highlights

* 🐘 PostgreSQL relational database
* 🐍 Python database integration
* 🎈 Interactive Streamlit UI
* ➕ Form-based order insertion
* ✅ Input validation
* 🔎 Custom SQL query execution
* 📊 Pandas DataFrame result display
* 🔐 Environment-based database configuration
* 🧩 Modular Python project structure
* 🧪 SQL testing and result verification
* 📚 Progressive SQL learning approach

---

## 📜 License

This project is created for educational and portfolio purposes.

Feel free to explore, modify, and extend it for your own learning.

```

**Important correction from your actual project:** I’ve described the status values as `Pending`, `Shipped`, `Delivered`, and `Cancelled`, because those are the values present in your actual `data_insertion.py`, rather than using the earlier sample dataset's `Completed` status.

This README now represents the project as it actually is: **SQL learning + PostgreSQL + Python + Streamlit UI**, not just an SQL query collection.
```
