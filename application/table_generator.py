# from application.extensions import db
# # from application.models.test import test_table
# from application import create_app
# app = create_app()
# db.drop_all(app=app)

from application.extensions import db
from application.models.test import test_table
# from application.models.aa import Role2
from start import app
with app.app_context():
    # db.drop_all()
    db.create_all()