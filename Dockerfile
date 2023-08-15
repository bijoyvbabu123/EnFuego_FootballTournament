FROM python:3.8-slim-buster

ENV PYTHONBUFFERED 1

# Set the working directory to /app
WORKDIR /django_app

# Copy the current directory contents into the container at /app
COPY . .

# Install any needed packages specified in requirements.txt without caching
RUN pip install --no-cache-dir -r requirements.txt

# # to keep the container running
# CMD tail -f /dev/null

# CMD [ "python3", "manage.py", "runserver" , "0.0.0.0:8000"]
