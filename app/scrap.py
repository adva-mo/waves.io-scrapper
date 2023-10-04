import os
from sqlalchemy import select
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, select
from app.models import users_subscriptions, User

load_dotenv()

db_url = os.environ.get("SQLALCHEMY_DATABASE_URI")
engine = create_engine(db_url)

Session = sessionmaker(bind=engine)
session = Session()

user_ids = set()
location_ids = set()
users_phone_numbers = {}


def get_user_subsrciptions_records():
    select_statement = select(users_subscriptions)
    results = session.execute(select_statement).fetchall()

    for result in results:
        user_id, location_id = result
        user_ids.add(user_id)
        location_ids.add(location_id)


def get_users_phone_numbers():
    select_statement = select(User.phone).where(User.id.in_(list(user_ids)))
    results = session.execute(select_statement).fetchall()
    for i, id in enumerate(user_ids):
        users_phone_numbers[id] = results[i][0]
    print(users_phone_numbers)
    session.close()
