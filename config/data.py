from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
load_dotenv(dotenv_path="config/dato.env")
user=os.getenv("MYSQL_USER")
password=os.getenv("MYSQL_PASSWORD")
host=os.getenv("MYSQL_HOST")
data_base=os.getenv("MYSQL_DATA_BASE")
db=SQLAlchemy()
DATA_BASE_URL= f"mysql+pymysql://{user}:{password}@{host}/{data_base}"                                                                       