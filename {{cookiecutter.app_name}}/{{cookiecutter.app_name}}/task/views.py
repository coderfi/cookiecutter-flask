# -*- coding: utf-8 -*-
from flask import Blueprint, render_template

blueprint = Blueprint("task", __name__, url_prefix='/tasks',
                        static_folder="../static")


@blueprint.route("/")
def tasks():
    return render_template("tasks/tasks.html")
