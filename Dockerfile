# Use the official Python image as a base
FROM python:3.11.4-slim-bullseye

# Set the working directory in the container
WORKDIR /app

# Update the package lists and install git
RUN apt-get update && apt-get install -y git

# Copy the requirements file into the container at /app
COPY ./requirements.txt /app/

# Upgrade pip and install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app
