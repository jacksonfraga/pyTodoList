from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


def init_db(app):
    db_uri = app.config['SQLALCHEMY_DATABASE_URI']
    if not hasattr(app, 'engine') :
        app.engine = create_engine(db_uri)
    app.engine.connect()
    db_session = sessionmaker(bind=app.engine)
    return db_session()
