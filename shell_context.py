from server import app
from quiz_card.extensions import db
from quiz_card.cards.models import Card
from quiz_card.timer.models import Timers


@app.shell_context_processor
def shell_context():
    return {'app':app, 'db':db, 'card':Card, 'timer':Timers}
