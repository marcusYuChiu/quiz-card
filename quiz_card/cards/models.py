from quiz_card.extensions import db
from quiz_card.timer.models import Timers


class Card(db.Model):
    __tablename__ = 'card'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(255), nullable=True)
    answer = db.Column(db.String(255), nullable=True)
    timer = db.relationship('Timers', backref='card', lazy=True)


    def __repr__(self):
        return '<CARD ID {}>'.format(self.id)
