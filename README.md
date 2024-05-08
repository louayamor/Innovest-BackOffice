# Django Project README

This repository contains a Django web application for managing users, businesses, investments, and sectors.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/louayamor/Innovest-BackOffice.git
   
Create a virtual environment (optional but recommended):
    ```bash
    python -m venv env

Activate the virtual environment:
On Windows:
    ```bash
    .\env\Scripts\activate
On macOS/Linux:
    ```bash
    source env/bin/activate

Set up the Django project:
    ```bash
    python manage.py migrate
    python manage.py createsuperuser
Run the development server:
    ```bash
    python manage.py runserver
Usage
Once the development server is running, you can access the following URLs:

Admin Panel: http://localhost:8000/admin/
Dashboard: http://localhost:8000/dashboard/
Users: http://localhost:8000/users/
Businesses: http://localhost:8000/businesses/
Investments: http://localhost:8000/investments/
Sectors: http://localhost:8000/sectors/

Features

User authentication and authorization
CRUD operations for users, businesses, and investments
Dashboard with data visualization (charts)
Sector-wise statistics and pie charts
Contributing
Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes and commit them (git commit -am 'Add new feature').
Push to the branch (git push origin feature-branch).
Create a new Pull Request.
