
from app.models import Question, Answer
from app.forms import QuestionForm, AnswerForm
from datetime import datetime
from flask import Blueprint, render_template, request, url_for
from werkzeug.utils import redirect

from app import db



fisa = Blueprint('basic', __name__, url_prefix = '/')





@fisa.route('/')
def index():
    return render_template('index.html')




