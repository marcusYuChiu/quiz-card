import json


from flask import Blueprint, render_template, redirect, url_for


from .forms import CreateForm
from .models import Card, MemoryStatus
from quiz_card.extensions import db


blueprint = Blueprint("card", 
                      __name__, 
                      url_prefix="/card",
                      template_folder="templates")

@blueprint.route('/')
def card():
    card_lst = Card.query.all()
    return render_template('card_views/card_view.html', card_lst=card_lst)


@blueprint.route('/create', methods=['GET', 'POST'])
def create():
    form = CreateForm()
    if form.validate_on_submit():
        new_card = Card(question=form.question.data,
                        answer=form.answer.data,
                        link=form.link.data)
        db.session.add(new_card)
        db.session.commit()
        return redirect('/card/')
    return render_template('card_views/create_card.html', form=form) 


@blueprint.route('/menu')
def menu():
    return render_template('card_views/menu.html')


@blueprint.route('/menu/<string:color>')
def practice_menu_color(color):
    if color in [m.value for m in MemoryStatus]:
        return render_template('card_views/color.html', color=color)
    return "We do not have this color"


@blueprint.route('/result')
def result():
    return




