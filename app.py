import os
import sys
from flask import Flask, jsonify
from flask_migrate import Migrate
from dotenv import load_dotenv
from extension import db  # Import db instance from models package
from flask_debugtoolbar import DebugToolbarExtension
import subprocess
from sqlalchemy import text


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

# Initialize database and migration once
db.init_app(app)
migrate = Migrate(app, db)

# API endpoint to initialize migrations
@app.route('/initialize-migrations', methods=['POST'])
def initialize_migrations():
    try:
        # Check if the migrations directory already exists
        if os.path.exists('migrations'):
            return jsonify({"message": "Migrations folder already exists."}), 200

        # Initialize migrations folder
        subprocess.run(["flask", "db", "init"], check=True)
        return jsonify({"message": "Migrations have been initialized."}), 200
    except subprocess.CalledProcessError as e:
        return jsonify({"error": f"Failed to initialize migrations: {str(e)}"}), 500

# Define the migrate-db endpoint
@app.route('/migrate-db', methods=['POST'])
def migrate_db():
    try:
        # Apply pending migrations
        subprocess.run(["flask", "db", "migrate", "-m", "Auto migration"], check=True)
        subprocess.run(["flask", "db", "upgrade"], check=True)
        return jsonify({"message": "Database migration has been applied."}), 200
    except subprocess.CalledProcessError as e:
        return jsonify({"error": f"Failed to migrate DB: {str(e)}"}), 500

# Define the reset-db endpoint
@app.route('/reset-db', methods=['POST'])
def reset_db():
    try:
        result = subprocess.run(["python", "reset_db.py"], check=True, capture_output=True, text=True)
        return jsonify({"message": "Database has been reset.", "output": result.stdout}), 200
    except subprocess.CalledProcessError as e:
        return jsonify({"error": f"Failed to reset database: {str(e)}", "details": e.stderr}), 500

@app.route('/refresh-db', methods=['POST'])
def refresh_db():
    try:
        # Run reset_db.py to reset the database
        subprocess.run(["python", "reset_db.py"], check=True)

        # Remove the migrations directory if it exists
        if os.path.exists('migrations'):
            import shutil
            shutil.rmtree('migrations')

        # Reinitialize the migrations folder
        subprocess.run(["flask", "db", "init"], check=True)

        # Generate a new initial migration
        subprocess.run(["flask", "db", "migrate", "-m", "Initial migration"], check=True)

        # Apply the migration to the database
        subprocess.run(["flask", "db", "upgrade"], check=True)

        return jsonify({"message": "Database has been refreshed and migrations applied."}), 200

    except subprocess.CalledProcessError as e:
        return jsonify({"error": f"Failed to refresh database: {str(e)}", "details": e.stderr}), 500

@app.route('/apply-model-changes', methods=['POST'])
def apply_model_changes():
    try:
        subprocess.run(["flask", "db", "migrate", "-m", "Model changes auto-migration"], check=True)
        subprocess.run(["flask", "db", "upgrade"], check=True)
        return jsonify({"message": "Model changes detected and applied to database."}), 200
    except subprocess.CalledProcessError as e:
        return jsonify({"error": f"Failed to apply model changes: {str(e)}", "details": e.stderr}), 500

@app.route('/resolve-migration-desync', methods=['POST'])
def resolve_migration_desync():
    try:
        result = subprocess.run(["flask", "db", "stamp", "head"], check=True, capture_output=True, text=True)
        print("STAMP STDOUT:", result.stdout)
        print("STAMP STDERR:", result.stderr)

        subprocess.run(["flask", "db", "migrate", "-m", "Apply on-top model changes"], check=True)
        subprocess.run(["flask", "db", "upgrade"], check=True)

        return jsonify({"message": "Migration synced and model changes applied on top of existing schema."}), 200

    except subprocess.CalledProcessError as e:
        return jsonify({
            "error": "Subprocess command failed.",
            "details": e.stderr or str(e)
        }), 500
    except Exception as e:
        return jsonify({
            "error": "Unexpected server error.",
            "details": str(e)
        }), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5051)
