import os
import time

# from dotenv import load_dotenv
# from sqlalchemy import create_engine, select
from app.scrap import get_user_subsrciptions_records, get_users_phone_numbers

# from sqlalchemy.orm import sessionmaker

# load_dotenv()
# db_url = os.environ.get("SQLALCHEMY_DATABASE_URI")
# engine = create_engine(db_url)
# Session = sessionmaker(bind=engine)
# session = Session()


def create_app():
    while True:
        get_user_subsrciptions_records()
        get_users_phone_numbers()
        time.sleep(10)
