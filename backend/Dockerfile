FROM python:3.10.2
WORKDIR /code
COPY . /code
RUN pip install -r requirements.txt
CMD gunicorn foodgram.wsgi:application --bind 0.0.0.0:8000