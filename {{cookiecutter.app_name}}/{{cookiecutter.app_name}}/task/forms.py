from flask_wtf import Form
from wtforms import TextField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from {{cookiecutter.app_name}}.database import dbmongo

from .models import User

class TaskForm(Form):
    title = TextField('Title',
                    validators=[DataRequired(), Length(min=3, max=25)])
    text = TextField('Text',
                    validators=[DataRequired(), Length(min=6, max=255)])

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.task = None

    def validate(self):
        initial_validation = super(TaskForm, self).validate()
        if not initial_validation:
            return False
        task = dbmongo.Task.find_one({'title':title})
        if task:
            self.task.errors.append("Task already exists")
            return False

        self.task = task
        return True
