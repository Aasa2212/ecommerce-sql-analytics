# E-Commerce SQL Analytics Project

## About This Project

This project simulates an e-commerce business database and analyzes customer, sales, product, and shipment data using PostgreSQL.

The goal was to practice writing real-world SQL queries and understand how businesses use data to make decisions.

Instead of using a public dataset, I generated the data using Python and Faker, then loaded it into PostgreSQL for analysis.



## Dataset

The database contains:

| Table | Records |
|---------|---------:|
| Customers | 100 |
| Orders | 500 |
| Order Items | 1000 |
| Payments | 500 |
| Shipments | 500 |
| Products | 6 |
| Categories | 5 |


## Database Structure

The project uses the following tables:

- customers
- orders
- order_items
- products
- categories
- payments
- shipments

Relationships were created using primary and foreign keys to simulate a real e-commerce system.



## SQL Concepts Used

Throughout this project I practiced:

- INNER JOINs
- GROUP BY
- Aggregate Functions
- CASE Statements
- Window Functions (RANK)
- Common Table Expressions (CTEs)
- Views
- Sorting and Filtering
- Business Analytics Queries


## Analysis Performed

### Top Spending Customers

Identified customers who generated the highest revenue.

### Customer Segmentation

Grouped customers into:

- VIP
- Regular
- New

based on their total spending.

### Revenue by Product Category

Calculated which product categories generated the most revenue.

### Top Selling Products

Ranked products based on total units sold.

### Monthly Revenue Analysis

Tracked revenue trends over time.

### Delivery Analysis

Measured shipment performance using shipped and delivered dates.



## Technologies Used

- PostgreSQL
- Python
- Pandas
- Faker
- Git
- GitHub
- VS Code



## Sample Business Questions Answered

- Who are the highest-value customers?
- Which products sell the most?
- Which categories generate the most revenue?
- What is the average order value?
- How does revenue change over time?
- How quickly are orders delivered?



## What I Learned

This project helped me understand how SQL is used beyond simple queries. I worked with multiple related tables, created reusable views, wrote analytical queries, and generated realistic data using Python.

It also gave me hands-on experience with Git and GitHub for project version control.



## Future Improvements

- Increase dataset size to tens of thousands of records
- Build Power BI dashboards
- Add customer retention analysis
- Add inventory and return tracking
- Deploy the project with automated data generation
