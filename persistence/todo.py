from models.todo import Todo


class TodoPersistence:

    def __init__(self, app):
        self.session = app.db_session

    def create(self, data):
        todo = Todo(**data)
        self.session.add(todo)
        self.session.commit()
        return todo

    def get_all(self, filter=None):
        query = self.session.query(Todo)
        if filter is not None:
            query = query.filter_by(**filter)
        return query.all()

    def update(self, todo_id, data):
        self.session.query(Todo). \
            filter(Todo.todo_id == todo_id). \
            update(data)
        self.session.commit()
        return self.session.query(Todo). \
            filter(Todo.todo_id == todo_id).first()

    def delete(self, todo_id):
        affected_rows = self.session.query(Todo). \
            filter(Todo.todo_id == todo_id). \
            delete()
        self.session.commit()
        return {'success': affected_rows > 0, 'affected_rows': affected_rows}
