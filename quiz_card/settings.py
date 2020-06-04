import tempfile
from environs import Env

env = Env()
env.read_env()

ENV = env.str("FLASK_ENV", default="developement")
DEBUG = ENV == "development"
SQLALCHEMY_DATABASE_URI = env.str("DATABASE_URL")
SECRET_KEY = env.str("SECRET_KEY")
SQLALCHEMY_TRACK_MODIFICATIONS = False
# DBFD, DATABASE = tempfile.mkstemp()
# TESTING = True
