# UWVisionBackend

## Running project locally

### Prerequisites:
- Install Python 3.10.0: `pyenv install 3.10.0` (assuming you have pyenv setup)
- Set your local Python env to the version installed: `pyenv local 3.10.0`
- Upgrade to the latest pip: `python -m pip install --upgrade pip`
- Install Django: `python -m pip install django`
- Install Django REST Framework: `python -m pip install djangorestframework`
- Install Django CORS Headers: `python -m pip install django-cors-headers`
- Install Psycopg2: `python -m pip install psycopg2`
- Setup Postgres server:
  - Visit https://postgresapp.com/downloads.html and download the `Postgres.app with PostgreSQL 14 (Universal)`
  - Once application is downloaded, hit initialize to start a server (remember you can stop it at any time)
  - Enter in terminal: `export PATH=$PATH:/Applications/Postgres.app/Contents/Versions/latest/bin`

### First-time setup
- Activate virtual environment: `source django_env/bin/activate`
- Install requirements `python -m pip install -r requirements.txt`
  - NOTE: You may get `Building wheel for backports.zoneinfo (PEP 517) ... error` - that's okay for now
- Ensure that your Potgres App server is on
- Run `python manage.py migrate` to get your database initialized
- Create a superuser for yourself: `python manage.py createsuperuser`
- Run `python manage.py runserver` to get started with the server

### Running it after the initial setup
- Activate your virtual environment: `source django_env/bin/activate`
  - On the left of your terminal prompt, you will see the environment activated `(django_env) ...`
- Make sure your Postgres server is running (hit start in the app to do so)
- Use any of the regular Django commands after (ex: `python manage.py runserver`)

