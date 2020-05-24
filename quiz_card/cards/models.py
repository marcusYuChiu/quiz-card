import enum
from datetime import datetime


from quiz_card.extensions import db

# tags = db.Table('tags',
    # db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True),
    # db.Column('card_id', db.Integer, db.ForeignKey('card.id'), primary_key=True)
# )

class MemoryStatus(enum.Enum):
    red = 'red'
    green = 'green'
    yellow = 'yellow'
    blue = 'blue'


class Card(db.Model):
    __tablename__ = 'card'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(255), nullable=False)
    answer = db.Column(db.String(255), nullable=False)
    link = db.Column(db.String(255), nullable=False)
    created_time = db.Column(db.DateTime,
                             default=datetime.utcnow(),
                             nullable=False)
    weight = db.Column(db.Float(1), default=0, nullable=False)
    memory_status = db.Column(db.Enum(MemoryStatus),
                              default=MemoryStatus.blue,
                              nullable=False)
    # tag_id = db.relationship('Tag',
                             # secondary=tags,
                             # lazy='subquery',
                             # backref=db.backref('pages',
                                                # lazy=True))
                              #uselist=False)

    def __repr__(self):
        return '<CARD ID {}>'.format(self.id)


# class Tag(db.Model):
    # __tablename__ = 'tag'
    # id = db.Column(db.Integer, primary_key=True)
    # name = db.Column(db.String(50))
    
    # def __repr__(self):
        # return '<TAG Name {}>'.format(self.self.name)
