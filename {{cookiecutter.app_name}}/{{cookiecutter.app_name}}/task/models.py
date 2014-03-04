# -*- coding: utf-8 -*-
import datetime as dt

from {{cookiecutter.app_name}}.database import dbm, CRUDMixinMongo
from flask.ext.mongokit import Document
from datetime import datetime

@dbm.register
class Task(Document, CRUDMixinMongo):
    #__database__ = 'xyzabc'
    __collection__ = 'tasks'

    structure = {
        'title': unicode,
        'text': unicode,
        'creation': datetime,
    }
    required_fields = ['title', 'creation']
    default_values = {'creation': datetime.utcnow}
    use_dot_notation = True

    def __repr__(self):
        return '<Task "{title}">'.format(title=self.title)


