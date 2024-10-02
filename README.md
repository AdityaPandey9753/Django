# Django Complete

## Installation
* Install uv -> An extremely fast Python package and project manager, written in Rust.
* uv venv -> create virtual env with name .venv
* .venv\Scripts\activate -> to activate virtual env
* uv pip install django -> Download Django in virtual wrapper, if uv not used it would install globally
* django-admin startproject DjangoFirst
* uv pip freeze > requirements.txt

## File structure
```
my_project/
├── manage.py
└── my_project/
    ├── __init__.py
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```
* manage.py - <br>This is the entry point for managing the Django project. It is the file that is invoked first. It provides commands like running the development server, creating new apps, migrating data and more.
* my_project - <br>This directory contains the core settings and configuration files for your project.
* __init__.py - <br>This empty file denotes that the my_project directory is a Python package.
* asgi.py - <br>This file is used to manage asynchronous request in the project. It is primarily used for modern web framework and asynchronous task.
* settings.py - <br>This is the central configuration file for the project. Contains setting related to database connections, installed apps, template directories, static file and more.
* urls.py - <br>This define the url pattern for your project. It maps the url to specific views.
* wsgi.py - This file handles synchronous request in your application. Used for traditional web servers.