import os
from flask import Flask
from flask_migrate import Migrate
from dotenv import load_dotenv
from models import db  # Import db instance from models package
from flask_debugtoolbar import DebugToolbarExtension

import sys
import os

# Add the models directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'models'))

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False  # Prevents redirecting
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'DEV'



# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@"
    f"{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

toolbar = DebugToolbarExtension(app)
# Initialize database and migration
db.init_app(app)  # Initialize the db instance with the app
migrate = Migrate(app, db)

# Migration creation and upgrade
if __name__ == '__main__':
    # Start the Flask application
    # app.run(host='0.0.0.0', port=5051)
    try:
        print("Database Migration successfully.")
    except Exception as e:
        print(f"An error occurred while resetting the database: {e}")
        sys.exit(1)  # Exit with an error status code
    finally:
        sys.exit(0)  # Exit with success status code
