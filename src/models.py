from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Todo(db.Model):
    __tablename__ = 'todo'
    id = db.Column(db.Integer, primary_key=True)
    todo = db.Column(db.String(120), nullable=False)
    status = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return '<Todo %r>' % self.id
    
    def serialize(self):
        return {
            "id": self.id,
            "todo": self.todo,
            "status": self.status
        }

    