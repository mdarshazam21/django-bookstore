# Online Bookstore

A Django-based e-commerce bookstore application featuring a session-based shopping cart, guest and authenticated checkout, and order history with database-level aggregation.

## Features

- Browse books with cover images, pricing, and stock information
- Session-based shopping cart (works without requiring login)
- Guest checkout or checkout while logged in
- Order history for authenticated users, with totals calculated via database aggregation
- Fully responsive design using CSS Grid and Flexbox

## Setup

1. Clone this repository
2. Create a virtual environment: `python -m venv .venv`
3. Activate it: `.\.venv\Scripts\activate` (Windows) or `source .venv/bin/activate` (Mac/Linux)
4. Install dependencies: `pip install -r requirements.txt`
5. Run migrations: `python manage.py migrate`
6. Create a superuser: `python manage.py createsuperuser`
7. Run the server: `python manage.py runserver`

## Tech Stack

- Django 6.1
- SQLite
- HTML/CSS (Grid & Flexbox)