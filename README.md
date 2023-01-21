# assessment

you can run this codebase by using following command

$ docker-compose up --build

if you want to stop the containers use the following command
$ docker-compose down

to run test run the following command
$docker-compose run --rm app sh -c "coverage run manage.py test && coverage report"

to run any command:
$ docker-compose run --rm app sh -c "<your command>"