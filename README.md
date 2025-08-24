# HopCognitracker

## Table of Contents
-----------------

* [Overview](#overview)
* [Features](#features)
* [Requirements](#requirements)
* [Installation](#installation)
* [Usage](#usage)
* [Folder Structure](#structure)
* [Contributing](#contributing)

## Overview
------------

HopCognitracker is a web-based application designed to facilitate the management of medical questionnaires and patient results. The platform aims to streamline the process of creating, administering, and tracking medical questionnaires. With HopCognitracker, medical professionals can easily create and customize questionnaires, assign them to patients, and track responses in real-time.

## Features
------------

- The project is optimized for the Greek translation of "The Johns Hopkins Dementia Care Needs Assessment (JHDCNA) MIND Streamlined-CLINICAL" questionnaire.
- There's simple auth, a dashboard showing newest additions to doctors, patients, questionnaires and attempts.
- List and detail django views and forms make up the majority of the functionality.
- Admin panel and user created attempts automatically populate the relevant answer models for the selected questionnaire.

## Requirements
- [Python](https://www.python.org/downloads/)
- [Django](https://www.djangoproject.com/)

## Installation
------------

1. Clone or download the repository to your local machine:
```bash
git clone https://www.github.com/devpersi/Thesis
```
2. Open a terminal and create a [virtual environment](https://docs.python.org/3/library/venv.html)
```bash
# e.g.
python -m venv venv
```
3. Activate it
```
| Platform | Shell       | Command to Activate Virtual Environment       |
|----------|-------------|-----------------------------------------------|
| POSIX    | bash/zsh    | `$ source venv/bin/activate`                  |
|          | fish        | `$ source venv/bin/activate.fish`             |
|          | csh/tcsh    | `$ source venv/bin/activate.csh`              |
|          | pwsh        | `$ venv/bin/Activate.ps1`                     |
| Windows  | cmd.exe     | `C:\> venv\Scripts\activate.bat`              |
|          | PowerShell  | `PS C:\> venv\Scripts\Activate.ps1`  		 |
```
4. Install requirements
```bash
pip install -r requirements.txt
```
5. Run the application
```bash
py manage.py runserver
```
6. Visit http://127.0.0.1:8000/ or http://localhost:8000/ in a browser

## Usage
-----

After running the application you are met with a landing page asking you to login.

Back in the terminal create an admin by filling in some details:
```bash
# Run
py manage.py createsuperuser
# Fill in some details
Username: admin
Email address: admin@example.com
Password: **********
Password (again): *********
# You should see this message:
Superuser created successfully.
```

Log in to your account and you are met with a landing page asking you to click to see the medical index.  
In the medical index, There are lists of the most recent Doctors, Patients, Questionnaires and Attempts.  
Clicking the name of a list e.g. Doctors will show the full lists with the ability to edit or create more entries.  
In order to see all this, you need to populate the database with models. For now, you can  
- add doctors and patients
- visit the [admin](http://127.0.0.1/admin) dashboard provided by django and 
- add a questionnaire along with questions pointing to it with their foreign key
- go back to the attempts and you will be able to create attempts based on the newly created questionnaire, each with its own set of answers




## Structure
--------

All important files are in the medical directory:

- medical
  - templates
    - base_medical.html
    - attempt.html
    - attempts.html
    - doctor.html
    - doctors.html
    - index.html
    - patient.html
    - patients.html
    - questionnaire.html
    - questionnaires.html
  - admin.py
  - forms.py
  - models.py
  - forms.py
  - urls.py
  - views.py
  - views_create_edit.py
  - services
    - attempt_services.py


## Contributing
------------

\#TBD