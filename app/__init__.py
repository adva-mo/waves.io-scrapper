import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()
db_url = os.environ.get("SQLALCHEMY_DATABASE_URI")


def create_app():
    engine = create_engine(db_url)
    print("app created")
