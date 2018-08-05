from sqlalchemy import create_engine, Table, Column, Integer, String, Boolean, MetaData


def create_db():
    db_uri = 'sqlite:///db/production.sqlite3'  # current_app.config['SQLALCHEMY_DATABASE_URI']
    engine = create_engine(db_uri, echo=True)
    engine.connect()

    metadata = MetaData()

    todos = Table('todos', metadata,
                  Column('todo_id', Integer, primary_key=True),
                  Column('description', String(255), nullable=False),
                  Column('done', Boolean, nullable=False, default=False)
                  )

    todos.create(engine, checkfirst=True)
