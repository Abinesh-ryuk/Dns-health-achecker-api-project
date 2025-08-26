from pymongo import MongoClient # TO Import MongoClient to connect to MongoDB
import os # To Import os to read environment variables
from dotenv import load_dotenv# To Import dotenv to load variables from .env file

load_dotenv() # To Load environment variables from .env file
client = MongoClient(os.getenv("MONGO_URI"))# Create MongoDB client using URI from .env
db = client[os.getenv("DB_NAME")]#TO Select database using name from .env
collection = db["analyses"]# To Select collection to store DNS analysis results
