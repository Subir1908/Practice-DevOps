# Base image with Python pre-installed
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy your project files into the container
COPY src/ ./src/

# Command to run your application
CMD ["python", "src/tracker.py"]