from quiz_card.extensions import db


class Timers(db.Model):
    __tablename__ = 'timer'
    id = db.Column(db.Integer, primary_key=True)
    created_time = db.Column(db.DateTime, nullable=False)
    card_id = db.Column(db.Integer, db.ForeignKey('card.id'), nullable=False)


    def __repr__(self):
        return '<Timer ID {}>'.format(self.id)
