import os

DB_USERNAME = os.getenv('POSTGRES_USERNAME', 'postgres')
DB_PASSWORD = os.environ.get('POSTGRES_PASSWORD', 'password')

SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USERNAME}:{DB_PASSWORD}@localhost:5432/doggie_db'
