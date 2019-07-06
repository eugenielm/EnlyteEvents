EnlyteEvents
=================

Small Django project that allows the user to pull events from Eventbrite and store them on a local database.
It also allows to update existing events, as well as search/filter these events via a RESTful API.
The API is implemented with the Django REST framework.
It's using a postgreSQL database, which is suitable for production, unlike Django's default sqlite3 database.

The project was tested locally with Python 3.7.2.



How it works
------------

1. Make sure you have Python 3+ installed on your computer (it may or may not work with
Python versions older than 3.7.2) and pip

2. Fork this repo

3. Database pre-requisites:
- make sure posgreSQL is installed on your machine
Note: this project uses the psycopg2 package that supports PostgreSQL server versions from 7.4 to 11
and the PostgreSQL client library version from 9.1
(http://initd.org/psycopg/docs/install.html#prerequisites)
- launch the posgreSQL server and create a new database for this project
- update the DATABASES settings in settings.py

4. In your terminal, go to the EnlyteEvents/ directory:
```sh
cd ~/path/to/EnlyteEvents/
```

5. Install the dependencies by running the command below (you might want to create a virtual
environment before running it):
```sh
pip install -r requirements.txt
```

6. Set the projects's secret key (a string containing any characters) either as an environment variable by running:
```sh
export $SECRET_KET=<my_secret_key>
```
or by creating a text file called 'secret_key.txt' containing the key in a directory
called 'settings_var/' (located at the root of the project)

7. Apply the migrations by running:
```sh
python manage.py migrate
```

8. Launch the dev server (if no port number is specified, it will run on port 8000 by default)
```sh
python manage.py runserver [port_number]
```

9. To access the schema of the API, open a web browser and go to: 'http://localhost:8000/api/schema'
(replace 8000 by the right port number if necessary)


How to populate the database
----------------------------
A custom django-admin command has been implemented to populate the database with events
pulled from Eventbrite.

1. Optional: in the terminal, go to the root directory of the project and set the Eventbrite API
Oauth token as an environment variable by running:
```sh
export $EVENTBRITE_OAUTH_TOKEN=<token>
```

1. then run:
```sh
python manage.py fetchevents [--number_of_events num] [--token oauth_token_to_access_the_eventbrite_api]
```
If the environment variable EVENTBRITE_OAUTH_TOKEN is not set, then you need to use the optional argument --token


By default, running this command will store 500 unique events from Eventbrite in the database.
The events will have the following fields:
- name
- organization
- cost: an integer that's the average of the minimum_ticket_price and the maximum_ticket_price
- start_date: the start_date of the Eventbrite event (a DateField, not a DateTimeField)
- event_original_id: a read-only field with a unique constraint; this is the Eventbrite event's id, to
make sure 2 identical events can't be stored in case the `fetchevents` command is run several times



To be improved
--------------

- add some tests


More info about the Django web framework:
https://www.djangoproject.com/start/

More info about Django REST framework:
https://www.django-rest-framework.org/
