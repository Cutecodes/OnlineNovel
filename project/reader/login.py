from .reader import *
from .models import login as login_verify
@reader.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        reader = request.form['readerName']
        password = request.form['readerPassword']
        if login_verify(reader,password):
            response = make_response(redirect(url_for('reader.readercenter')))
            response.set_cookie('readerName',reader,max_age=3600)
            response.set_cookie('readerPassword',password,max_age=3600)
            
            return response
        else:
            return "密码或账号错误"

    else:
        return render_template('reader_login.html')