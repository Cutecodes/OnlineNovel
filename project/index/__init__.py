

from .index import _index
from .novel import *
from .chapter import *
from .search import *

def init_app(app):

    app.register_blueprint(_index)