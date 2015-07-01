from flask import Blueprint


bp = Blueprint('modis', __name__)


@bp.route('/')
def discovery():
    return 'Hello, Blueprint!'