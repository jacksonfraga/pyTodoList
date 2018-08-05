from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean

Base = declarative_base()


class Todo(Base):
    __tablename__ = 'todos'

    todo_id = Column(Integer, primary_key=True)
    description = Column(String(255), nullable=False)
    done = Column(Boolean, nullable=False, default=False)

    def __init__(self, todo_id=None, description=None, done=None):
        self.description = description
        self.done = done
        self.todo_id = todo_id

    def __repr__(self):
        return '<Todo %r>' % self.description

    def to_dict(self):
        return {
            'todo_id': self.todo_id,
            'description': self.description,
            'done': self.done
        }
