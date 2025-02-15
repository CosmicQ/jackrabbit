# Use a Python base image
FROM python:3.9-slim

# Install required packages
RUN pip install pymongo flask

# Copy the Python service file
COPY mongo_service.py /app/mongo_service.py

# Set the working directory
WORKDIR /app

# Expose port 5000 for the Flask app
EXPOSE 5000

# Run the app
CMD ["python", "mongo_service.py"]

