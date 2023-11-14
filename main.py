import os
from db.db import DB
from dotenv import load_dotenv

load_dotenv()
db = DB(os.getenv('DB_USER'), os.getenv('DB_PASSWORD'), os.getenv('DB_HOST'), os.getenv('DB_PORT'),
        os.getenv('DB_NAME'))

session = db.get_session()
print(session.info)
