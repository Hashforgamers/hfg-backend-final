#!/bin/bash


set -e  # Exit immediately if any command fails

# Ensure required environment variables are set
if [ -z "$DB_USER" ] || [ -z "$DB_NAME" ]; then
    echo "Error: DB_USER and DB_NAME environment variables must be set."
    exit 1
fi

# Export the Flask app variable
export FLASK_APP=app.py


# # Handle commands passed as arguments
# case "$1" in
#     "refresh")
#         echo "Refreshing migrations and database..."

#         # Call thace reset function from the reset_db script
#         python reset_db.py

#         # Reinitialize migrations
#         echo "Initializing migrations folder..."
#         flask db init

#         # Create and apply the initial migration
#         echo "Creating initial migration..."
#         flask db migrate -m "Initial migration"
#         echo "Running database migrations..."
#         flask db upgrade
#         ;;
        
#     "reset")
#         echo "Resetting database and deleting migrations folder..."
        
#         # Call the reset function from the reset_db script
#         python reset_db.py
#         ;;

#     *)
#         # Initialize migrations folder if it doesn't exist
#         if [ ! -d "migrations" ]; then
#             echo "Initializing migrations folder..."
#             flask db init
#         fi

#         # Auto-generate migrations if there are model changes
#         echo "Creating migrations if necessary..."
#         flask db migrate -m "Auto migration"

#         # Apply migrations
#         echo "Running database migrations..."
#         flask db upgrade
#         ;;
# esac

# # Start the Flask application
echo "Starting the Flask application..."
exec python app.py
