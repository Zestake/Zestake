from flask import Blueprint

landing_page_bp = Blueprint('landing_page', __name__)

@landing_page_bp.route("/")
def landing_page():
    return "<h1>Zestake</h1>"
