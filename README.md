 # Library Management System

## Overview
This is a simple Library Management System developed using the Frappe framework. The system allows libraries to manage books, members, and loans efficiently with an intuitive user interface and custom REST API.

## Core Features
### Book Management
- Create, read, update, and delete (CRUD) operations for books.

### Membership Management
- CRUD operations for members.

### Loan Management
- Track book loans with fields like Member, Book, Loan Date, and Return Date.
- Check book availability before loaning.

### Reports
- Generate reports for all currently loaned books and overdue books.
### Custom API Development
- REST API for interacting with the system externally.
- Supports adding, retrieving, updating, and deleting books and members.
- Includes authentication for secure access.

### User Interface
- User login interface with email/username and password authentication.
- Dashboard for displaying available books.
- Book details view.

## Setup Instructions
### Prerequisites
Ensure you have the following installed:
- Python (3.10+ recommended)
- Node.js and npm
- Redis
- MariaDB
- wkhtmltopdf

### Installation Steps
1. **Install Frappe Bench**
   ```sh
   pip install frappe-bench
   ```

2. **Initialize a Bench and Create a Site**
   ```sh
   bench init lms-bench
   ```
   ```sh
     cd lms-bench
   ```
   ```sh
   bench new-site lms.localhost
   ```

4. **Get the Custom Library Management App**
   ```sh
   cd apps
   ```

      ```sh
  git clone https://github.com/ClickWithMuleta/Library_Management_System_Challenge-360-Ground-.git
 ```
  
   cd ..
```

```sh
   bench get-app library_management_system
```
   ```sh
   bench --site lms.localhost install-app library_management_system
   ```

4. **Run the Development Server**
   ```sh
   bench start
   ```

5. **Access the Application**
   Open a browser and go to: `http://lms.localhost:8000`
   
