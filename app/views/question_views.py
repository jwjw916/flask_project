
from app.models import Question, Answer
from app.forms import QuestionForm, AnswerForm
from datetime import datetime
from flask import Blueprint, render_template, request, url_for
from werkzeug.utils import redirect

from app import db



ques = Blueprint('question', __name__, url_prefix = '/ques')





@ques.route('/create/', methods=('GET', 'POST'))
def create():
    form = QuestionForm()
	# create 함수로 요청된 전송 방식     #  폼 데이터의 정합성 점검
    if request.method == 'POST' and form.validate_on_submit():
        question = Question(subject=form.subject.data, content=form.content.data, create_date=datetime.now())
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('question.success'))
    return render_template('question/question_form.html', form=form)


@ques.route('/success')
def success():
    question_list = Question.query.all()
    return render_template('question/question_list.html', question_list=question_list)


@ques.route('/detail/<int:question_id>/')
def detail(question_id):
    form = AnswerForm()
    question = Question.query.get_or_404(question_id)
    return render_template('question/question_detail.html', question=question, form=form)

@ques.route('/list')
def _list():
    page = request.args.get('page', type=int, default=1)  # 페이지네이션
    question_list = Question.query.order_by(Question.create_date.desc())
    question_list = question_list.paginate(page=page, per_page=10)
    return render_template('question/question_list.html', question_list=question_list)