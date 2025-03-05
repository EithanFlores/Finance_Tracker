# Personal Finance Tracker

## Video: https://drive.google.com/file/d/1l5sisdzOdmJod9wU4JaN__xPeeL5UCo0/view?usp=sharing

The Personal Finance Tracker is a web application designed to help users manage their income and expenses in an efficient and organized way. The application allows users to add transactions, filter them based on their type (Income or Expense), and visualize their financial data through interactive charts. The goal of this project is to provide users with an intuitive interface where they can track their spending habits, analyze their income distribution, and make informed financial decisions.

This project is built using Flask as the backend framework, SQLAlchemy for database management, and Matplotlib for generating data visualizations. The user interface is designed using HTML, CSS, and Jinja templates to ensure a clean and responsive layout. Users can input transactions with a title, description, and amount, and all data is stored in a SQLite database. The homepage displays all transactions in a table format, along with filter options to switch between all transactions, only income, or only expenses. Two dynamic charts are included: a pie chart showing the proportion of income vs. expenses, and a bar chart that breaks down spending into categories.

One of the key features of this application is the ability to delete transactions using a simple and intuitive ❌ icon instead of a traditional button. This improves the user experience by making the interface more visually appealing and reducing clutter. The application also includes error handling to prevent crashes when no transactions exist, ensuring that empty states are handled properly.

The core logic of the application is in the project.py file. This file includes the Flask routes for adding, deleting, and displaying transactions, as well as the SQLAlchemy model that defines the Transaction table in the database. It also contains the logic for generating visualizations using Matplotlib, including functions that calculate total income and expenses and create dynamic charts based on user data.

The index.html template is the main user interface where transactions are displayed in a table format. It includes filters that allow users to view only income, only expenses, or all transactions. Each transaction entry includes a delete button in the form of a red ❌ icon, which allows users to remove unwanted transactions. The page also dynamically loads the pie chart and bar chart using base64-encoded images generated in the backend.

The add_transaction.html template is responsible for handling new transactions. It provides a form where users can enter a transaction type, title, description, and amount before submitting it. Once submitted, the transaction is stored in the database and immediately reflected on the homepage.

The styles.css file contains all the custom styling for the application. It enhances the overall layout by ensuring proper spacing, adding color themes, and improving the appearance of buttons and filters. The delete button and filter options are also styled for better user experience. The navigation bar includes a simple and clean layout, featuring a logo that makes the application look more professional.

One of the design choices made in this project was the inclusion of filters for managing transactions. Initially, the app only displayed all transactions together, making it difficult to differentiate between income and expenses. By adding filters, users can now quickly switch between different transaction types, improving usability. Another key design decision was implementing a visual representation of financial data through Matplotlib charts. This helps users gain insights into their financial habits at a glance, rather than having to manually analyze transaction records.

Several challenges were encountered during development. One of the major issues was handling cases where no transactions existed in the database, which initially caused Matplotlib to throw errors when generating charts. This was resolved by adding error handling that prevents chart generation when there are no transactions, displaying a placeholder message instead. Another challenge was ensuring that transaction deletion updates the UI properly without requiring a page refresh. This was solved by properly handling database commits and redirections after deleting a transaction.

The finance tracker can be expanded in several ways. Future improvements could include implementing user authentication so that multiple users can track their finances independently. Another useful addition would be the ability to edit transactions instead of just deleting them. Users could also set financial goals and track their progress over time, providing a more comprehensive financial planning tool. A dark mode toggle could be introduced to enhance the UI and improve accessibility.

In conclusion, the Personal Finance Tracker is a simple but effective tool for managing personal finances. It combines Flask for backend logic, SQLAlchemy for database management, and Matplotlib for data visualization. The application allows users to track income and expenses, filter transactions, and view dynamic charts for financial insights. The user interface is designed to be clean and intuitive, making financial tracking simple and efficient.

Through this project, I have gained experience in working with Flask, database integration using SQLAlchemy, and creating dynamic web applications with Jinja templates. I also learned how to handle errors effectively, optimize database queries, and implement interactive visualizations with Matplotlib. Overall, this project has helped me build a deeper understanding of web development and data management, and I look forward to expanding its functionality in the future.

