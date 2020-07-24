from flask import render_template, redirect, flash
from flask_login import login_user, logout_user, current_user

from flask_app import db
from flask_app.auth import bp
from flask_app.auth.forms import LoginForm, RegistrationForm
from flask_app.models import User


@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if current_user.is_authenticated:
        redirect('/index')

    if form.validate_on_submit():
        print(form.username)
        print(form.password)
        user = User.query.filter_by(username=form.username.data).first()
        if user is None:
            return redirect('/login')

        if not user.check_password(form.password.data):
            return redirect('/login')

        login_user(user)
        return redirect('/index')

    return render_template('auth/login.html', title='Sign In', form=form)


@bp.route('/logout')
def logout():
    logout_user()
    return redirect('/index')


@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User()
        user.username = form.username.data
        user.email = form.email.data
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect('/login')

    return render_template('auth/register.html', title='Sign In', form=form)
