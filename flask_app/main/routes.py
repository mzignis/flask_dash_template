from flask import render_template, redirect
from flask_login import login_required, logout_user

from flask_app.main import bp


@bp.route('/index')
@bp.route('/home')
@bp.route('/')
@login_required
def index():
    return redirect('/dash/')


@bp.route('/dash')
@login_required
def dashboard():
    redirect('/dash/')

