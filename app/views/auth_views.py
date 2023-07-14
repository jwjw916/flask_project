
from app.models import User
from app.forms import UserForm, LoginForm
from flask import Blueprint, render_template, request, url_for, redirect, flash, session, g
from app import db

from flask_login import LoginManager
login_manager = LoginManager()


auth_user = Blueprint('user', __name__, url_prefix = '/user')

@auth_user.route('/signup', methods=(['GET', 'POST']))
def sign_up():
    form = UserForm()

    if request.method== 'POST' and form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if not user:
            user = User(username=form.username.data, password=form.password1.data, email=form.email.data)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('basic.index'))
        else:
            flash('이미 존재하는 사용자입니다.', category="error")
    return render_template('user/signup.html', form=form)


@auth_user.route("/login", methods=(["POST", "GET"]))
def log_in():
    form = LoginForm()

    if request.method== 'POST' and form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if user.password == form.password.data:
                session.clear()
                session['user_id'] = user.id
                flash('로그인 성공입니다.',category="success")
                return redirect(url_for('basic.index'))
        else:
            flash('아이디 또는 비밀번호를 확인하세요', category="error")
    else:
        flash('아이디 또는 비밀번호를 확인하세요', category="error")

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