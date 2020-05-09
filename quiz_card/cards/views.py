import json


from flask import Blueprint, render_template


from .models import Card


blueprint = Blueprint("card", 
                      __name__, 
                      url_prefix="/card",
                      template_folder="templates")

@blueprint.route('/')
def card():
    card_lst = Card.query.all()
    return render_template('card_views/card_view.html', card_lst=card_lst)










