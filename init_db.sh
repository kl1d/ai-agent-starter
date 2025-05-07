#!/bin/bash
DB_PATH="/app/data/sample.db"

# Check if the database already exists
if [ ! -f "$DB_PATH" ]; then
    echo "Initializing SQLite database..."
    sqlite3 "$DB_PATH" <<EOF
CREATE TABLE customers (
    id INTEGER PRIMARY KEY,
    name TEXT,
    purchase_amount REAL,
    purchase_date TEXT
);

INSERT INTO customers (name, purchase_amount, purchase_date)
VALUES 
    ('Alice', 1200, '2025-04-01'),
    ('Bob', 900, '2025-03-15'),
    ('Charlie', 1500, '2025-04-20');
EOF
    echo "Database initialized."
else
    echo "Database already exists. Skipping initialization."
fi

# Start the Flask app
exec python web/app.py
