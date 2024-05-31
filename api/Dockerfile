# Use the official Python 3.8 image from the Docker Hub as the base image
FROM python:3.8

# Copy the contents of the current directory to the /app directory in the container
COPY . /app

# Set the working directory to /app
WORKDIR /app

# Install the Python dependencies listed in requirements.txt
RUN pip install -r requirements.txt

# Expose port 5000 to allow external access to this port on the container
EXPOSE 5000

# Define the command to run the application when the container starts
CMD ["python", "api.py"]
