FROM python:3.10-slim
WORKDIR /app

# Install SQLite CLI
RUN apt-get update && apt-get install -y sqlite3 && rm -rf /var/lib/apt/lists/*

# Set Python environment
ENV PYTHONPATH=/app

# Install dependencies
COPY web/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all files
COPY . .

# Make the script executable
RUN chmod +x /app/init_db.sh

EXPOSE 5000

# Use the init script as the entry point
CMD ["/app/init_db.sh"]
