from flask import render_template

from flask_app.errors import bp

@bp.app_errorhandler(404)
def error_404(error):
    return render_template('errors/404.html'), 404