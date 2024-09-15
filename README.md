# Affyn's Blog Site

Welcome to Affyns's Blog Site, a fully-fledged online blog site designed with a sleek and user-friendly interface. This project combines a sophisticated front-end built with HTML, CSS, Bootstrap, and JavaScript, and a robust Python Django backend.

## Key Features

* Responsive Design: Built using Bootstrap for a seamless experience across various devices and screen sizes.
* Interactive UI: Dynamic and engaging user interface with smooth transitions and intuitive controls.
* Secure Backend: Django backend ensures a secure and scalable architecture for handling site data.
* Account Management: Users can easily create accounts, and manage profiles.
* Standard Comment System: Users can easily make comments on posts, edit, delete and can also make and receive replies.
* Post Reaction: Users can easily react and remove reaction from posts.
* Search Feature: Posts can be easily searched with title, writer and category.
* Standard Sorting: Posts are easily sorted by categories.
* and many more...

## Technologies Used

- **Frontend:** HTML, CSS, Bootstrap, JavaScript
- **Backend:** Python Django
- **Database:** SQLite (can be easily configured for other databases)

## Getting Started

### 1. Clone the repository:
    git clone https://github.com/PeterOlayemi/blog_site.git

### 2. Install dependencies:
    pip install -r requirements.txt

### 3. Create environment variables (.env) file containing these variables (all vars are set to an empty string for testing purpose only):
    SECRET_KEY = '{{your_django_project_secret_key}}'
    my_email = '{{your_email_address}}'
    appsPassword = '{{your_appspassword_for_email}}'

### 4: Migrate server:
    python manage.py makemigrations
    python manage.py migrate

### 5: Run the development server:
    python manage.py runserver

### 6: Access the application at http://localhost:8000

## Contributing
Feel free to contribute by submitting issues or pull requests.

## License
This project is licensed under the [MIT License](LICENSE) - see the [LICENSE](LICENSE) file for details.

# Where to find Me
[Visit My Website](https://peterolayemi.github.io)
