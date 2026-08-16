# 📚 Online Bookstore with Shopping Cart

A full-featured Django e-commerce application for browsing books, managing a session-based shopping cart, and completing checkout — supporting both guest and authenticated users.

## Features

- **Book Catalog** — Browse books with cover images, descriptions, pricing, and stock tracking
- **Session-Based Shopping Cart** — Add/remove items without requiring login, powered by Django sessions
- **Search** — Find books by title or ingredients using `Q` object queries
- **Checkout System** — Guest and authenticated checkout, converting cart data into permanent orders
- **Order History** — Logged-in users can view past orders with totals calculated via database-level aggregation (`Sum`, `F` expressions)
- **Live Cart Counter** — Custom Django template tag displaying real-time cart item count in the header
- **Responsive Design** — CSS Grid-based catalog layout with hover animations and a consistent design system
- **Admin Panel** — Full management of books, orders, and order items via Django's built-in admin

## Tech Stack

- **Backend:** Python, Django
- **Database:** SQLite (development)
- **Frontend:** HTML, CSS (Grid & Flexbox), Django Templates
- **Image Handling:** Pillow

## Project Structure
bookstore-project/
├── bookstore_site/ # Project configuration (settings, URLs)
├── store/ # Main app
│ ├── models.py # Book, Order, OrderItem models
│ ├── views.py # Book, cart, and checkout views
│ ├── cart.py # Session-based Cart class
│ ├── forms.py # OrderCreateForm
│ ├── templatetags/ # Custom cart_item_count tag
│ ├── templates/store/ # HTML templates
│ └── static/store/ # CSS
├── media/ # Uploaded book cover images (not tracked in Git)
├── manage.py
├── requirements.txt
└── .env.example


## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/YourUsername/bookstore-project.git
cd bookstore-project
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
.\.venv\Scripts\Activate     # Windows
source env/bin/activate   # macOS/Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Copy `.env.example` to a new file named `.env`, then fill in your own values:



### 5. Run migrations

```bash
python manage.py migrate
```

### 6. Create a superuser

```bash
python manage.py createsuperuser
```

### 7. Run the development server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

## Usage

- Browse books on the homepage or use the search bar to find specific titles/ingredients
- Add books to your cart — no account required
- Proceed to checkout as a guest, or log in first to link the order to your account
- Log in and visit `/orders/` to view your past order history
- Access `/admin/` with your superuser account to manage books, orders, and inventory

## Key Django Concepts Demonstrated

- Django sessions for stateful, login-free shopping carts
- Custom model fields (`DecimalField`, `PositiveIntegerField`, `ImageField`)
- Database aggregation with `Sum` and `F` expressions
- Custom template tags
- `ModelForm` and file upload handling
- Django admin customization

## License

This project is for educational purposes.