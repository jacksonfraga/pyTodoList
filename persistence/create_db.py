from sqlalchemy import create_engine, Table, Column, Integer, String, Boolean, MetaData


def create_db(app):
    # db_uri = 'mysql+pymysql://bbddd2acec8c7f:d38988f70b18b9e@us-cdbr-iron-east-01.cleardb.net/heroku_78038307a9708b3'
    db_uri = app.config['SQLALCHEMY_DATABASE_URI']
    engine = create_engine(db_uri, echo=True)
    engine.connect()

    metadata = MetaData()

    todos = Table('todos', metadata,
                  Column('todo_id', Integer, primary_key=True),
                  Column('description', String(255), nullable=False),
                  Column('done', Boolean, nullable=False, default=False)
                  )

    todos.create(engine, checkfirst=True)
