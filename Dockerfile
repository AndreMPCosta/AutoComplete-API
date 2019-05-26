# Use an official Python runtime as a parent image
FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7

# Install any needed packages
RUN pip3 install pipenv

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

#Install dependencies
RUN pipenv install --system --deploy

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "app.py"]