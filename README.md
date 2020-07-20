# flask-boilerplate
  Flask Boilerplate to quickly get started with production grade flask application with some additional packages and configuration prebuilt 

# Prerequisites

- Python 3.8.2 or higher
- Up and running Redis client

# Virtual Env

- Install `pipenv` a global python project `pip install pipenv`
- Create a `virtual environment` for this project
```shell
# creating pipenv environment for python 3
$ pipenv --three
# activating the pipenv environment
$ pipenv shell
# install all dependencies (include -d for installing dev dependencies)
$ pipenv install -d
```

# Running app

- Run flask app `python run.py`
- Logs would be generated under `log` folder

# Running celery

- Run redis locally before running celery worker
- celery worker -A celery_worker.celery -l=info  (append `--pool=solo` for windows)

# Configuration

- There are 3 configurations `development`, `staging` and `production` in `config.py`. Default is `development`
- Create a `.env` file from `.env.example` and set appropriate environment variables before running the project

# Includes Preconfigured Packages

- celery
- redis
- flask-cors
- python-dotenv
- marshmallow
- webargs
- autopep8 & flake8 as `dev` packages for `linting and formatting`

# Test
Test if this app has been installed correctly and it is working via following curl commands (or use in Postman)
- Check if the app is running via `status` API
```shell
$ curl --location --request GET 'http://localhost:5000/status'
```
- Check if core app API and celery task is working via
```shell
$ curl --location --request GET 'http://localhost:5000/api/v1/core/test'
```
- Check if authorization is working via (change `API Key` as per you `.env`)
```shell
$ curl --location --request GET 'http://localhost:5000/api/v1/core/restricted' --header 'x-api-key: 436236939443955C11494D448451F'
```