from .admin import _admin


def init_app(app):

    app.register_blueprint(_admin,url_prefix='/admin')