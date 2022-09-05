from .init_sqlalchemy import init_database, db


def init_plugs(app):
    init_database(app)
