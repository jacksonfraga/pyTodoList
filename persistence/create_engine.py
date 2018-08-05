from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


def init_db(app):
    db_uri = app.config['SQLALCHEMY_DATABASE_URI']
    engine = create_engine(db_uri)
    engine.connect()
    Session = sessionmaker(bind=engine)
    app.db_session = Session()
    Base.metadata.create_all(engine)
