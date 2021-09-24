from .reader import *
from .models import login as login_verify
from .models import get_bookshelf
@reader.route('/bookshelf',methods=['POST','GET'])
def readerbookshelf():
    reader = request.cookies.get('readerName')
    password = request.cookies.get('readerPassword')
    if login_verify(reader,password):
        novels = get_bookshelf(reader)
        return render_template('reader_bookshelf.html',novels=novels)
    else:
        return render_template('reader_login.html')
    