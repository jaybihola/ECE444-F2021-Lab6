# create_db.py


from Project.app import db
from Project.models import Post


# create the database and the db table
db.create_all()

# commit the changes
db.session.commit()
