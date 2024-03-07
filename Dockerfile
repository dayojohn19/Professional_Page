FROM python:3


COPY . DOCKERWORKDIR
WORKDIR DOCKERWORKDIR
RUN pip install -r requirements.txt
# OLD
CMD ["python3","manage.py","runserver","0.0.0.0:8000"]
