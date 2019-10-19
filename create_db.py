# create_db.py
from app import db

# create the database and its table(s)
db.create_all()

# commit the changes
db.session.commit()
