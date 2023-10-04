import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, select, column
from sqlalchemy.orm import sessionmaker

load_dotenv()
db_url = os.environ.get("SQLALCHEMY_DATABASE_URI")
engine = create_engine(db_url)
Session = sessionmaker(bind=engine)
session = Session()


def create_app():
    from app.models import users_subscriptions

    select_statement = select(users_subscriptions)

    results = session.execute(select_statement).fetchall()

    for result in results:
        user_id, location_id = result
        print(f"User ID: {user_id}, Location ID: {location_id}")

    session.close()
