from .author import author
from .login import *
from .register import *
from .authorcenter import *
from .createnovel import *
from .authornovel import *
from .authorchapter import *
from .createchapter import *
from .updatechapter import *
from .index import *

def init_app(app):

    app.register_blueprint(author,url_prefix='/author')