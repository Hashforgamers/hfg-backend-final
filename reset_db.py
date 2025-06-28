from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

import os
import sys

# Database configuration (use the same DB URL as in your app)
DATABASE_URI = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"

def reset_database():
    engine = create_engine(DATABASE_URI)
    Session = sessionmaker(bind=engine)

    # Use a session to execute the drop schema command
    with Session() as session:
        session.execute(text("DROP SCHEMA public CASCADE; CREATE SCHEMA public;"))
        session.commit()  # Commit the changes

if __name__ == '__main__':
    try:
        reset_database()
        print("Database reset successfully.")
    except Exception as e:
        print(f"An error occurred while resetting the database: {e}")
        sys.exit(1)  # Exit with an error status code
    finally:
        sys.exit(0)  # Exit with success status code
