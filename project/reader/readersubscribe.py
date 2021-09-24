from .reader import *
from .models import login as login_verify
from .models import get_subscribe
@reader.route('/subscribe',methods=['POST','GET'])
def readerssubscribe():
    reader = request.cookies.get('readerName')
    password = request.cookies.get('readerPassword')
    if login_verify(reader,password):
        chapters = get_subscribe(reader)
        return render_template('reader_subscribe.html',chapters=chapters)
    else:
        return render_template('reader_login.html')
    