EnlyteEvents
=================

Small Django project that allows the user to pull and store events from Eventbrite. It also allows to update existing events, as well as search/filter these events via a RESTful API.

The API is implemented with the Django REST framework. It's using a postgreSQL database, which is suitable for production, unlike Django's default sqlite3 database.

The project was tested locally with Python 3.7.2.


How it works
------------

1. Make sure you have Python 3+ installed on your computer (it may or may not work with Python versions older than 3.7.2) and pip

2. Fork this repo, and from your terminal go to the EnlyteEvents/ directory
```sh
cd ~/path/to/EnlyteEvents/
```

3. Install the dependencies by running the command below (you might want to create a virtual environment before running it):
```sh
pip install -r requirements.txt
```

4. Set the projects's secret key (a string containing any characters) as an environment variable, either by running:
```sh
export $SECRET_KET=<my_secret_key>
```
or by creating a text file called 'secret_key.txt' containing the key in a directory called 'settings_var/' (located at the root of the project)

5. Apply the migrations by running:
```sh
python manage.py migrate
```

6. Launch the dev server (if no port number is specified, it will run on port 8000 by default)
```sh
python manage.py runserver [port_number]
```

7. To access the schema of the API, open a web browser and go to: 'http://localhost:8000/api/schema'
(replace 8000 by the right port number if necessary)


To be improved
--------------

- add some tests


More info about the Django web framework:
https://www.djangoproject.com/start/

More info about Django REST framework:
https://www.django-rest-framework.org/
