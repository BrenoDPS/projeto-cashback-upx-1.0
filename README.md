# Public Transport Usage Incentive System via Cashback

## Summary
This repository contains a system to encourage the use of public transport through cashback, where users are rewarded with a percentage of the amount deposited into their account, promoting public transport usage in cities. Regarding the project's code, the Django framework was used to build the backend, and Django Template was used for the frontend.

## Repository Structure
The repository structure is organized as follows:

```
projeto-cashback-upx-1.0/
│
│
├── cashback/                          # Directory containing files that define general settings and URL configurations.
│
├── core/                              # Directory containing the application's "core," including key files such as "models.py," which defines the project's models or
│   │                                  # entities, and "views.py," which defines the views responsible for making the application RESTful.
│   │                                 
│   ├── migrations/                    # Contains the database migration records, i.e., all changes made in "models.py".
│   │
│   └── templates/                     # Contains the files responsible for the frontend
│       └── core/
│
├── media/                             # Contains image files, i.e., static files stored in this folder
│
├── static/                            # Directory containing styling files, which are also static
│
├── templates/                         # Main frontend file that gathers all other components
│
├── tests/                             # Integration tests
│   ├── test_data_processing.py        # Tests for preprocessing
│   └── conftest.py                    # Global configurations and fixtures
│
├── db.sqlite3                         # Database file
├── manage.py                          # File that helps execute commands and apply the ORM concept
├── README.md                          # Project documentation
└── .gitignore                         # Ignore unnecessary files in Git
```

## Step 1: Clone the Repository
   
```bash
git clone https://github.com/BrenoDPS/projeto-cashback-upx-1.0.git
cd projeto-cashback-upx-1.0
```

## Step 2: Create a Virtual Environment

Navigate to the backend directory and run the following command:

```bash
python3 -m venv venv
```

## Step 3: Activate Virtual Environment

- On macOS/Linux:

```bash
source venv/bin/activate
```

- On Windows:

```bash
venv\Scripts\activate
```

You should see (venv) appear at the beginning of your command prompt, indicating that the virtual environment is active.

## Step 4: Install Requirements

```bash
pip install -r requirements.txt
```

## Step 5: Make the Migrations

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

## Step 6: Run the Server

```bash
python manage.py runserver
```

By default, the server will run on <http://127.0.0.1:8000/>.

## Step 7: Deactivate Virtual Environment

```bash
deactivate
```

---

Feel free to get in contact if you need any assistance!
