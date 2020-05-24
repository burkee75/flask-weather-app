# Dockerfile for Flask Weather App: https://github.com/burkee75/flask-weather-app

# Python
FROM python:3.8

RUN pip install pipenv

WORKDIR /usr/local/src/

# Copy Pipfiles
RUN which python
RUN python --version

# Copy Github Files
COPY *  /flask-weather-app/

EXPOSE 5000

WORKDIR /usr/local/src/flask-weather-app/
ENV FLASK_APP="weather_app.py"
RUN pipenv run flask run --host='192.168.1.250'
