# 🍽️ Sayli's Restaurant — Django Web Application

A Django-based restaurant web application developed as a college mini-project.

The application was independently implemented using Django, with the Little Lemon restaurant website used as a reference for the overall restaurant concept and UI inspiration.

## 📌 Project Overview

Sayli's Restaurant is a web application that stores and displays restaurant dishes dynamically using Django and SQLite.

The application demonstrates core Django concepts, including models, database interaction, CRUD operations, forms, Function-Based Views (FBV), Class-Based Views (CBV), URL configuration, Django Template Language (DTL), template inheritance, static files, and Django Admin.

## ✨ Features

- 🏠 Home page
- 🍽️ Dynamic restaurant menu
- 🔎 Search dishes using a query parameter
- ➕ Add a new dish
- ✏️ Edit an existing dish
- 🗑️ Delete a dish with confirmation
- 📂 Dish categories
- 💾 SQLite database using Django ORM
- 📝 Django ModelForm
- 🔐 Django Admin dashboard
- 🎨 CSS styling
- 🖼️ Restaurant and food images
- 🔗 Navigation between pages
- 📄 Template inheritance using base.html

## 🛠️ Technologies Used

- Python
- Django
- SQLite
- HTML
- CSS
- Django Template Language (DTL)

## 🗃️ Database Models

The project contains two main models:

### Category

Stores restaurant dish categories.

### Dish

Stores dish information, including:

- Name
- Price
- Category

Each Dish belongs to a Category through a ForeignKey relationship.

### Database Relationship

text
Category (1) ───────── (*) Dish


One category can contain multiple dishes, while each dish belongs to one category.

## 🔄 CRUD Operations

The project demonstrates CRUD functionality for dishes:

| Operation | Implementation |
|-----------|----------------|
| Create | Add Dish form |
| Read | Dynamic Menu |
| Update | Edit Dish |
| Delete | Delete Dish with confirmation |

## 👩‍💻 Django Concepts Demonstrated

- Django project and app structure
- Models and relationships
- Django ORM
- CRUD operations
- Function-Based Views (FBV)
- Class-Based Views (CBV)
- Project-level and app-level URL configuration
- Dynamic URL parameters
- Query parameters
- HTTP request methods and forms
- Django Template Language (DTL)
- Template inheritance
- ModelForm
- Static files
- Django Admin

## 🚀 How to Run

### 1. Clone the repository

bash
git clone https://github.com/saylikamble180/Saylis-Restaurant-Django.git


### 2. Navigate to the project directory

bash
cd Saylis-Restaurant-Django


### 3. Install dependencies

bash
pip install -r requirements.txt


### 4. Apply database migrations

bash
python manage.py migrate


### 5. Start the development server

bash
python manage.py runserver


### 6. Open the application

Open the following address in your browser:

text
http://127.0.0.1:8000/


### Django Admin

To access Django Admin, open:

text
http://127.0.0.1:8000/admin/


Create an administrator account first if necessary:

bash
python manage.py createsuperuser


## 📸 Screenshots

### Home Page
<img width="536" height="377" alt="Screenshot 2026-10-02 194933" src="https://github.com/user-attachments/assets/37da7099-4982-4a83-a1fe-af909da803c5" />

### Menu
<img width="467" height="429" alt="Screenshot 2026-10-02 193901" src="https://github.com/user-attachments/assets/47b72208-f3b3-48c7-884a-f1b1ac8b825f" />

### Add Dish
<img width="212" height="302" alt="Screenshot 2026-10-02 193709" src="https://github.com/user-attachments/assets/7adfc826-ea3c-4ac0-adf5-872fd11ada15" />


## 📚 Reference Website

*Little Lemon Restaurant Website*

The website was used as a reference for the restaurant application's overall concept and layout. The Django implementation was developed independently.

## 🎓 Project Information

- *Project Type:* College Mini-Project
- *Framework:* Django
- *Subject:* Python Web Development Framework – Django

## 👩‍💻 Author

*Sayli Kamble*
