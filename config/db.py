from distutils.log import debug
import pdb
import ssl
import certifi
from pymongo import MongoClient
from dotenv import load_dotenv
from os import environ

load_dotenv()

db_user = environ.get("DATABASE_USER")
db_passwd = environ.get("DATABASE_PASSWORD")
db_server = environ.get("DATABASE_SERVER")

db_connection = MongoClient(
  f"mongodb+srv://{db_user}:{db_passwd}@{db_server}",
  tlsCAFile=certifi.where()
  )


