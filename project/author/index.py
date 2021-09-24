from .author import *
from .models import login as login_verify
from .models import get_author
@author.route('/',methods=['POST','GET'])
def index():
    return redirect(url_for('author.authorcenter'))
    