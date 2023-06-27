# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install the required Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the bot script and requirements.txt to the container
COPY emacs_insert.py .
COPY telegram_fetcher.py .
COPY .env .

# Set the command to run your bot script
CMD [ "python", "telegram_fetcher.py" ]