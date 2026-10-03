# TasteHub

TasteHub is a full-stack recipe-sharing web application developed using Django and PostgreSQL. It allows users to discover recipes, create and manage their own recipes, and explore recipes from an external API.

## Features

- User registration and login
- Secure authentication using Django
- User dashboard
- Create, view, edit and delete recipes
- Recipe categories
- User ownership and authorisation
- Search and filter recipes
- External recipe integration using TheMealDB API
- Responsive design using Bootstrap 5
- PostgreSQL database
- Automated testing using Django's testing framework
- Git and GitHub version control

## Technologies Used

- Python
- Django
- PostgreSQL
- HTML5
- CSS3
- JavaScript
- Bootstrap 5
- TheMealDB API
- Git and GitHub

## Project Structure

The project is organised using Django's project and application structure.

- `config/` – Django project configuration
- `recipes/` – Main application containing models, views, forms, templates and tests
- `recipes/static/` – CSS, JavaScript and image files
- `recipes/templates/` – HTML templates
- `recipes/migrations/` – Database migrations
- `manage.py` – Django management commands
- `requirements.txt` – Python dependencies
- `render.yaml` – Deployment configuration

## Database

TasteHub uses PostgreSQL as its database. Django's ORM is used to create and manage the application's database models and relationships.

The main models include:

- **Recipe** – Stores recipe information and links each recipe to a category and user.
- **Category** – Stores recipe categories.

## External API

TasteHub integrates with **TheMealDB API** to allow users to explore additional recipes.

The Explore page retrieves recipes from the API and displays information such as:

- Recipe name
- Category
- Cuisine
- Image
- Full recipe details

Users can also search the external recipes using the search functionality.

## Authentication and Authorisation

Django's built-in authentication system is used for user registration and login.

Authenticated users can create and manage their own recipes. Users can only edit or delete recipes that they have created.

Unauthenticated users can browse the site but must log in to view full recipe details.

## Testing

Automated tests were created using Django's testing framework.

The tests cover key functionality including:

- Recipe model creation
- Home page loading
- User login
- Dashboard authentication
- Recipe creation

The test suite was run using:

`python manage.py test recipes`

All tests passed successfully.

## Responsive Design

Bootstrap 5 is used together with custom CSS to provide a responsive interface across desktop and mobile screen sizes.

The navigation bar, recipe cards, forms and other page elements adapt to smaller screen sizes.

## Version Control

Git and GitHub were used throughout development to track changes and maintain the project history.

Regular commits were made during development, with meaningful commit messages used to document progress.

Feature branches were used for individual development tasks. For example, automated testing was developed on the `feature/automated-testing` branch before being merged into the `main` branch.

The final project is maintained on GitHub:

https://github.com/jmichael2025/TasteHub

## Local Installation

Clone the repository:

`git clone https://github.com/jmichael2025/TasteHub.git`

Open the project folder and install the required dependencies:

`pip install -r requirements.txt`

Create and apply database migrations:

`python manage.py makemigrations`

`python manage.py migrate`

Run the development server:

`python manage.py runserver 8001`

The application can then be accessed locally at:

http://127.0.0.1:8001/

## Deployment

The application is intended to be deployed using Render with PostgreSQL.

Deployment configuration is provided in `render.yaml`.

After deployment, the hosted application should be tested to confirm that authentication, database operations, API integration and responsive pages work correctly in the production environment.

## Author

**Jasmin Michael**