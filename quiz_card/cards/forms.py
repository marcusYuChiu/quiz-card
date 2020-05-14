from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class CreateForm(FlaskForm):
    question = TextAreaField('Question',
                             class_="question_box",
                             validators=[DataRequired()])
    answer = TextAreaField('Answer',
                           class_="answer_box",
                           validators=[DataRequired()])
    link = TextAreaField('Link')
    submit = SubmitField('Submit')
