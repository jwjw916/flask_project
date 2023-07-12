from flask import Blueprint, render_template
from app.models import Question

fisa = Blueprint('basic', __name__, url_prefix = '/')

# @fisa.route('/about_me')
# def about_me():
#     return f'저는 {__name__}입니다.'

# 라우팅 주소를 만드실 때는 /경로명 까지만 적어줍니다. 
# 그 다음에 만들어질 하위 경로도 /경로명 
# @fisa.route('/hello')
# def hello():
#     return f'안녕하세요'

# @fisa.route('/bye')
# def bye():
#     return f'안녕히 가세요'



@fisa.route('/detail/<int:question_id>/')
def detail(question_id):
    question = Question.query.get_or_404(question_id)
    return render_template('question/question_detail.html', question=question)

@fisa.route('/list')
def post():
    question_list = Question.query.all()
    return render_template('question/question_list.html', question_list=question_list)

# /loop 라는 uri로 이동하는 화면을 만듭니다. 
# test.html 파일로 가게 됩니다. test = [ 1, 2, 3, 4, 5] 라는 리스트를 같이 return 합니다. 


@fisa.route('/loop')
def loop():
    test = [1,2,3,4,5]
    return render_template('test.html', list=test)

@fisa.route('/about_me')
def about_me():
    return render_template('about_me.html')

