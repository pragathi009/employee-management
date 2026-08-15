# Employee Management System

A web-based Employee Management System built using Python and Flask. The application allows users to manage employee information through a simple web interface.

## Features

* Add new employees
* View employee records
* Update employee information
* Delete employee records
* Store employee data using SQLite
* Simple and responsive web interface
* Automated testing
* Docker support
* Jenkins CI/CD support

## Technologies Used

* Python
* Flask
* SQLite
* HTML
* CSS
* JavaScript
* Docker
* Jenkins
* Git & GitHub

## Project Structure

```text
employee-management/
│
├── static/              # CSS, JavaScript and static files
├── templates/           # HTML templates
├── tests/               # Application tests
├── app.py               # Main Flask application
├── employees.db         # SQLite database
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker configuration
├── Jenkinsfile          # Jenkins CI/CD pipeline
├── .gitignore           # Git ignored files
└── README.md            # Project documentation
```

## Installation

Clone the repository:

```bash
git clone <your-github-repository-url>
cd employee-management
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
python app.py
```

Then open the local URL shown in the terminal, usually:

```text
http://127.0.0.1:5000
```

## Run Tests

```bash
pytest
```

## Docker

Build the Docker image:

```bash
docker build -t employee-management .
```

Run the container:

```bash
docker run -p 5000:5000 employee-management
```

Then open:

```text
http://localhost:5000
```

## CI/CD

The project includes a `Jenkinsfile` for automating the build and testing process using Jenkins.

## Future Improvements

* Employee authentication
* Role-based access
* Search and filtering
* Employee profile management
* REST API
* Cloud deployment
* Automated CI/CD deployment

## Author

Pragathi
