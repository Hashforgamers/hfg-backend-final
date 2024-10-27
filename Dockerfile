# Dockerfile

FROM python:3.9-slim

# Install PostgreSQL client
RUN apt-get update && apt-get install -y postgresql-client && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files
COPY . .

# Set executable permissions for entrypoint.sh
RUN chmod +x entrypoint.sh

# Set entrypoint to the entrypoint script and allow command override
ENTRYPOINT ["./entrypoint.sh"]
CMD [""]  # Default empty command to allow argument override
