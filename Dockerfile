# Use a Debian-based image
FROM python:3.9-alpine

# Update pip to minimize dependency errors
RUN pip install --upgrade pip

# Set the working directory inside the container
WORKDIR /ipu-gpa-calculator

# Copy the contents into the working directory
COPY . .

# Run pip to install the dependencies of the Flask app
RUN pip install -r requirements.txt

EXPOSE 5000
# Define the command to start the container
CMD ["python", "app.py"]
