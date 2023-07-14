
from app.models import User
from app.forms import UserForm, LoginForm
from flask import Blueprint, render_template, request, url_for, redirect, flash, session, g
from werkzeug.security import generate_password_hash, check_password_hash
from app import db

from flask_login import LoginManager
login_manager = LoginManager()


auth_user = Blueprint('user', __name__, url_prefix = '/user')

@auth_user.route('/signup', methods=(['GET', 'POST']))
def sign_up():
    form = UserForm()

    if request.method== 'POST' and form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        email = User.query.filter_by(email=form.email.data).first()
        if not user and not email:
            user = User(username=form.username.data, password=generate_password_hash(form.password1.data, method='sha256'), email=form.email.data)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('basic.index'))
        else:
            flash('이미 존재하는 사용자입니다.', category="error")
    return render_template('user/signup.html', form=form)


#이메일 유효성 검사
# @auth_user.route('/signup', methods=(['GET', 'POST']))
# def sign_up():
#     if request.method == 'POST':
#         # form - input의 name 속성을 기준으로 가져오기
#         email = request.form.get('email')
#         username = request.form.get('username')
#         password1 = request.form.get('password1')
#         password2 = request.form.get('password2')

#         # 유효성 검사
#         if len(email) < 5 :
#             flash("이메일은 5자 이상입니다.", category="error")
#         elif len(username) < 2:
#             flash("사용자 이름은 8자 이상입니다.", category="error")
#         elif password1 != password2 :
#             flash("비밀번호와 비밀번호재입력이 서로 다릅니다.", category="error")
#         elif len(password1) < 7:
#             flash("비밀번호가 너무 짧습니다.", category="error")
#         else:
#             # Create User > DB
#             new_user = User(email=email, username=username, password=generate_password_hash(password1, method='sha256'))
#             db.session.add(new_user)
#             db.session.commit()
#             flash("회원가입 완료.", category="success")  # Create User -> DB
#             return redirect(url_for('basic.index'))

#     return render_template('user/signup.html')


@auth_user.route("/login", methods=(["POST", "GET"]))
def log_in():
    form = LoginForm()

    if request.method== 'POST' and form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                session.clear()
                session['user_id'] = user.id
                flash('로그인 성공입니다.',category="success")
                return redirect(url_for('basic.index'))
            else:
                flash('아이디 또는 비밀번호를 확인하세요', category="error")
    # else:
    #     flash('아이디 또는 비밀번호를 확인하세요', category="error")

    return render_template('user/login.html', form=form)


@auth_user.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get(user_id)


@auth_user.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('basic.index'))


import functools

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(*args, **kwargs):
        if g.user is None:
            _next = request.url if request.method == 'GET' else ''
            return redirect(url_for('auth.login', next=_next))
        else:
            return view(*args, **kwargs)
    return wrapped_view