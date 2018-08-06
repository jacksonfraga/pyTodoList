from models.todo import Todo
from persistence.create_engine import init_db


class TodoPersistence:

    def __init__(self, app):
        self.session = init_db(app)

    def create(self, data):
        todo = Todo(**data)
        self.session.add(todo)
        self.session.commit()
        return todo

    def get_all(self, filters=None):
        query = self.session.query(Todo)
        if filters is not None:
            query = query.filter_by(**filters)
        results = query.all()
        for item in results:
            self.session.expunge(item)
        return results

    def update(self, todo_id, data):
        self.session.query(Todo). \
            filter(Todo.todo_id == todo_id). \
            update(data)
        self.session.commit()
        todo = self.session.query(Todo). \
            filter(Todo.todo_id == todo_id).first()
        self.session.expunge(todo)
        return todo

    def delete(self, todo_id):
        affected_rows = self.session.query(Todo). \
            filter(Todo.todo_id == todo_id). \
            delete()
        self.session.commit()
        return {'success': affected_rows > 0, 'affected_rows': affected_rows}
