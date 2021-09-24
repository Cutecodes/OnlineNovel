from .editor import editor
from .login import *
from .editorcenter import *
from .editorcharge import *
from .chargechapter import *

def init_app(app):

    app.register_blueprint(editor,url_prefix='/editor')