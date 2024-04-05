FROM python:3.10

# Install git
RUN apt-get update && \
    apt-get install -y git

# Set working directory
WORKDIR /code

# Copy requirements file
COPY requirements.txt /tmp/requirements.txt

# Install Python dependencies
RUN set -ex && \
    pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    rm -rf /root/.cache/

# Copy the rest of your application code
COPY . /code
