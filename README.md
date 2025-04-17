# Library Management System

A Django-based Library Management System for managing books, students, and issued books. The system includes features for both administrators and students. Admins can manage students and books, while students can view their profile, change their password, and check issued books.

## Features

### Admin Features
- Admin can manage books (Add, Update, Delete).
- Admin can manage student profiles.
- Admin can view issued books and track due dates.
- Admin can register and authenticate students.

### Student Features
- Students can view their profile.
- Students can change their password.
- Students can view the books they have issued.
- Students can register and update their profile details.

## Technologies Used

- **Backend**: Django 4.2.7
- **Database**: SQLite (Deafault)
- **Frontend**: HTML, Bootstrap 5, DataTables.js
- **Libraries**:
  - Bootstrap for UI styling
  - DataTables.js for displaying and exporting tables

## Setup Instructions

### Prerequisites
Ensure you have the following installed:
- Python 3.x
- pip (Python package installer)
- Django 4.x
- MySQL (**optional**, for production deployment)

### 1. Clone the repository

```bash
git clone (https://github.com/SurabhiSharma4/Library-Managment-System)
cd library-management-system
