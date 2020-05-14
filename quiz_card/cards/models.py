import enum
from datetime import datetime


from quiz_card.extensions import db
from quiz_card.timer.models import Timers


class MemoryStatus(enum.Enum):
    red = 'red'
    green = 'green'
    yellow = 'yellow'
    blue = 'blue'


class Card(db.Model):
    __tablename__ = 'card'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(255))
    answer = db.Column(db.String(255))
    link = db.Column(db.String(255), nullable=True)
    created_time = db.Column(db.DateTime, default=datetime.utcnow())
    memory_status = db.Column(db.Enum(MemoryStatus),
                              default=MemoryStatus.blue,
                              nullable=False)
                              uselist=False)
    # tag_id = db.relationship('Tag',
                             # secondary=tags,
                             # lazy='subquery',
                             # backref=db.backref('pages',
                                                # lazy=True))

    def __repr__(self):
        return '<CARD ID {}>'.format(self.id)


# class Tag(db.Model):
    # __tablename__ = 'tag'
    # id = db.Column(db.Integer, primary_key=True)
    # name = db.Column(db.String(50))
    

