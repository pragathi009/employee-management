# Employee Management System

A simple web-based Employee Management System built with Flask and SQLite, with automated testing, Docker containerization, and Jenkins CI/CD.

## Overview

This project allows users to manage employee records through a web interface.

The application supports:

* Add employees
* View all employees
* Edit employee details
* Delete employees
* Employee dashboard
* SQLite database
* Automated testing using Pytest
* Docker containerization
* Jenkins CI/CD pipeline
* GitHub Webhook for automatic Jenkins builds

## Tech Stack

| Technology | Purpose                        |
| ---------- | ------------------------------ |
| Python     | Backend programming            |
| Flask      | Web framework                  |
| HTML/CSS   | Frontend                       |
| Bootstrap  | UI design                      |
| SQLite     | Database                       |
| Pytest     | Automated testing              |
| Docker     | Containerization               |
| Jenkins    | CI/CD                          |
| GitHub     | Source code management         |
| ngrok      | Local Jenkins webhook exposure |

## Project Structure

```text
employee-management/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── Jenkinsfile
├── .gitignore
│
├── templates/
│   ├── index.html
│   ├── add_employee.html
│   └── edit_employee.html
│
├── static/
│   └── style.css
│
└── tests/
    └── test_app.py
```

## Features

### Employee Dashboard

Displays all employees stored in the SQLite database.

### Add Employee

Users can add:

* Name
* Email
* Department
* Position

### Edit Employee

Existing employee information can be updated.

### Delete Employee

Employees can be removed from the database.

## Running Locally

Clone the repository:

```bash
git clone https://github.com/pragathi009/employee-management.git
```

Move into the project:

```bash
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

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Open:

```text
http://localhost:5000
```

## Running Tests

Run:

```bash
python -m pytest
```

The project currently includes tests for:

* Home page
* Adding an employee

## Docker

Build the Docker image:

```bash
docker build -t employee-management .
```

Run the container:

```bash
docker run -d -p 5000:5000 --name employee-app employee-management
```

Open:

```text
http://localhost:5000
```

Check running containers:

```bash
docker ps
```

## Jenkins CI/CD Pipeline

The project uses Jenkins to automate the application delivery process.

### Pipeline

```text
GitHub
   ↓
GitHub Webhook
   ↓
Jenkins
   ↓
Checkout Source Code
   ↓
Install Dependencies
   ↓
Run Pytest
   ↓
Build Docker Image
   ↓
Deploy Docker Container
```

### Jenkins Stages

#### 1. Checkout

Jenkins retrieves the latest source code from GitHub.

#### 2. Install Dependencies

Jenkins installs the Python packages from `requirements.txt`.

#### 3. Run Tests

Pytest runs the automated tests.

#### 4. Build Docker Image

Jenkins creates a Docker image named:

```text
employee-management
```

#### 5. Deploy Container

Jenkins stops and removes the previous container and starts a new container using the latest Docker image.

## Automatic Deployment

A GitHub Webhook is configured to trigger Jenkins whenever new code is pushed to the `main` branch.

Therefore:

```text
git push
   ↓
GitHub Webhook
   ↓
Jenkins automatically starts
   ↓
Tests
   ↓
Docker Build
   ↓
Docker Deployment
```

No manual **Build Now** action is required after the webhook is configured.

## Example Git Workflow

Make changes to the application:

```bash
git add .
git commit -m "feat: update employee dashboard"
git push origin main
```

The GitHub push automatically triggers the Jenkins pipeline.

## Testing Result

The Jenkins pipeline successfully runs the automated tests before creating the Docker image.

Example:

```text
============================= test session starts =============================
collected 2 items

tests/test_app.py ..     [100%]

2 passed
```

## Future Improvements

* Employee search and filtering
* User authentication
* Role-based access
* Employee profile pictures
* REST API
* PostgreSQL/MySQL database
* Jenkins notifications
* Deployment to a cloud platform

## Author

**Pragathi**
