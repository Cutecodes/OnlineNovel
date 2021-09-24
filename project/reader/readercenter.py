from .reader import *
from .models import login as login_verify
from .models import get_reader
@reader.route('/readercenter',methods=['POST','GET'])
def readercenter():
    reader = request.cookies.get('readerName')
    password = request.cookies.get('readerPassword')
    if login_verify(reader,password):
        reader = get_reader(reader)
        return render_template('reader_center.html',reader=reader)
    else:
        return render_template('reader_login.html')
    