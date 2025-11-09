# Schoolmuaid - MVP Version

Schoolmuaid is a Django-based school management system for students, teachers, subjects, and admin dashboards.  
_Current version: Minimum Viable Product (MVP) — core functionality._

Quick Overview:  
- Manage students, teachers, and subjects  
- Admin dashboard for easy control  
- Built with Django 5.2.x and SQLite  

> For full setup, usage, and developer guidance, see the sections below.

---

## Table of Contents

1. [Project Structure](#project-structure)  
2. [Prerequisites](#prerequisites)  
3. [Installation & Setup](#installation--setup)  
4. [Running the Project](#running-the-project)  
5. [Static & Media Files](#static--media-files)  
6. [Important Files & Directories](#important-files--directories)  
7. [Developer Notes](#developer-notes)  
8. [Edge Cases](#edge-cases)  
9. [Contributing](#contributing)  
10. [License & Contact](#license--contact)  
11. [References](#references)

---

## Project Structure

- core/ — general utilities and shared logic  
- StudentsApp/ — student management (templates: students_index.html, profile.html, etc.)  
- teachers/ — teacher and subject management  
- dashboard/ — admin dashboard  

---

## Prerequisites

- Python 3.8+ (Python 3.10+ recommended)  
- Django 5.2.x  
- SQLite (default database)  

> A requirements.txt is included with Django and Pillow.

---

## Installation & Setup

1. Clone the repository
`bash
git clone https://github.com/muaid773/School-Management-System.git
cd Schoolmuaid

2. Create and activate a virtual environment



python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

3. Install dependencies



pip install -r requirements.txt

4. Setup database



python manage.py makemigrations
python manage.py migrate

5. Create superuser (admin)



python manage.py createsuperuser

6. Set SECRET_KEY



Option 1: Generate using VUSKey.py


python VUSKey.py

Option 2: Set manually in _Schoolmuaid_/settings.py:


SECRET_KEY = "your-strong-secret-key"


---

Running the Project

python manage.py runserver

Open http://127.0.0.1:8000 in your browser.


---

Static & Media Files

Paths in settings.py:

STATIC_ROOT → static/

STATICFILES_DIRS → _Schoolmuaid_/static/

MEDIA_ROOT → media/


Collect static files


python manage.py collectstatic --noinput


---

Important Files & Directories

manage.py — Django management commands

_Schoolmuaid_/settings.py — project settings

StudentsApp/ — student app

teachers/ — teacher app

dashboard/ — admin dashboard

templates/ — global templates (base.html included)



---

Developer Notes

Inputs: SQLite DB, templates, static files

Outputs: Fully functional Django app with admin access

Common pitfalls:

Virtual environment not activated

Django not installed or wrong version

Python version mismatch




---

Edge Cases

Fresh database → always run migrate and createsuperuser

Missing media files → media/students/photos/ may be empty

No dev/prod environment separation currently



---

Contributing

1. Fork the repository


2. Create a branch (git checkout -b feature/your-feature)


3. Commit changes (git commit -m "Add feature")


4. Push branch (git push origin feature/your-feature)


5. Open a Pull Request




---

License & Contact

License: MIT (or specify your license)

Contact: muaidali773@gmail.com



---

References

Django Documentation

SQLite Documentation

Python Documentation


