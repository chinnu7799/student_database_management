# Student Database Management System

A robust, interactive, and modular **Student Database Management System** built with Python. This application applies clean Object-Oriented Programming (OOP) principles to simulate core database operations, providing an efficient way to track and manage student records via a Command-Line Interface (CLI).

---

## 🚀 Key Features

The system fully handles **CRUD (Create, Read, Update, Delete)** operations with built-in data handling:

* **Create Record:** Seamlessly add new student profiles with validation for unique Student IDs.
* **Read / View:** View all records in a cleanly formatted terminal table, or look up specific individual profiles instantly by ID.
* **Update Record:** Modify specific fields (Name, Age, Course, Grade) of existing records without altering other details.
* **Delete Record:** Safely remove a student profile from the dataset.
* **Data Persistence:** Automatically saves records to a local JSON file structure, ensuring information is retained even after closing the program.

---

## 🛠️ Architecture & Logic

- **Modular OOP Design:** Built using separate, clean classes for data structuring (`Student`) and database operations (`StudentDatabase`).
- **Dynamic File Serialization:** Uses Python's native `json` module to serialize runtime memory object states into clean, readable physical storage and deserialize them back on startup.
- **Input Resilience:** Basic conditional logic handling to maintain data types and skip empty update inputs gracefully.

---

## 📦 Getting Started

### Prerequisites
Make sure you have **Python 3.x** installed on your system.

### Installation & Run
1. Clone this repository to your local machine:
   ```bash
   git clone [https://github.com/your-username/student-database-management.git](https://github.com/your-username/student-database-management.git)