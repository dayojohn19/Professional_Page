FROM python:3


COPY . DOCKERWORKDIR
WORKDIR DOCKERWORKDIR
RUN pip install -r requirements.txt
# CMD ["python3","manage.py","runserver","0.0.0.0:8000"]
CMD daphne app:app --bind 0.0.0.0 --port $PORT