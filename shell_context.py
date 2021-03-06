import random


from flask_sqlalchemy import BaseQuery


from server import app
from quiz_card.extensions import db
from quiz_card.cards.models import Card, MemoryStatus
from quiz_card.cards.component import loader


question_sample = ['q{}'.format(i) for i in range(6)]
answer_sample = ['a{}'.format(i) for i in range(6)]
link_sample = ['http://www.{}.com'.format(path) for path in range(6)]


def gen_data(number):
    for i in range(number):
        question = random.choice(question_sample)
        answer = random.choice(answer_sample)
        link = random.choice(link_sample)
        memory_status = random.choice(['red', 'yellow', 'green', 'blue'])

        new_card = Card(question=question,
                        answer=answer,
                        link=link,
                        memory_status=memory_status)
        db.session.add(new_card)
        db.session.commit()
    return


def format_data(model, *args):
    '''
    Model 
    Arguments in args should match the attributes from models.
    '''
    output = []
    if isinstance(model, BaseQuery):
        data = model
    else:
        data = model.query.all()

    for line in data:
        formatted_line = ''
        for attr in range(len(args)):
            formatted_line += ('{} '.format(line.__dict__[args[attr]]))
        output.append(formatted_line) 
    return output


@app.shell_context_processor
def shell_context():
    return {
            'app': app,
            'db': db,
            'card': Card,
            'memory_status': MemoryStatus,
            'gen_data': gen_data,
            'format_data': format_data,
            'loader': loader
           }
