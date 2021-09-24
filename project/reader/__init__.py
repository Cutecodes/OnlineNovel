from .reader import reader
from .login import *
from .register import *
from .readercenter import *
from .readersubscribe import *
from .readerbookshelf import *

def init_app(app):

    app.register_blueprint(reader,url_prefix='/reader')