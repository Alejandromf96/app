from flask import (
    Blueprint, render_template, request, redirect, url_for
)

bp = Blueprint('portfolio', __name__, url_prefix='/')

@bp.route('/', methods=['GET'])
def index():
    return render_template('portfolio/index.html')

@bp.route('/contact', methods=['GET'])
def contact():
    return render_template('portfolio/contact.html')
