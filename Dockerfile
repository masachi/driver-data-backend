FROM python:alpine

EXPOSE 80

# Install gunicorn
RUN pip install gunicorn

# Install falcon
RUN pip install falcon

# Install requests
RUN pip install requests


COPY . /app
WORKDIR /app

CMD ["gunicorn", "-b", "0.0.0.0:80", "main:driver_data"]