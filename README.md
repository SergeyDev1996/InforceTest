## Installing of the app

Install PostgresSQL db and create db
```shell
git clone https://github.com/SergeyDev1996/InforceTest.git

python -m venv venv

venv/scripts/activate

pip install -r requirements.txt

set DB_HOST=<your db hostname>
set DB_NAME=<your db name>
set DB_USER=<your db username>
set DB_PASSWORD=<your db user password>
set SECRET_KEY=<your secret key>

python manage.py runserver
```
## Run with docker

Docker should be installed
```shell
docker-compose build
docker-compose up
```
## Creation of the user and access to the database

* To register a user: /api/user/register/

* To get access token: /api/user/token/
* To manage a user: /api/user/me/
* Please make sure to include "app-version: 1.0" or "app-version: 1.1" to your headers to access the api, otherwise it will not allow you to access any of the endpoints of the project. This is the requirement of the task.

## Other endpoints
* To get a list of the restaurants: /api/restaurant/ : GET

* To create a new restaurants: /api/restaurant/ :POST. You need to include {"name":"restaurant_name"} header to create a restaurant

* To vote for the restaurant: /api/vote/  :POST. You need to include {"name":"restaurant_name"} header to vote for the particular restaurant. As of now, 1 user can vote a few times.

* To upload a menu for the restaurant: /api/vote/ :PATCH. You need to include {"restraunt_name":"menu_/day/"}({"restraunt_name":"menu_monday"} as example) to add a menu for the current day

## Other things you need to know
* To get a menu of the restaurant for the current day, use :GET endpoint. The API will automatically choose a menu for today, if the one exists. 

