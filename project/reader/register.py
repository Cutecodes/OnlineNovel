from .reader import *
from .models import register as register_fn
@reader.route('/register',methods=['POST','GET'])
def register():
    if request.method == 'POST':
        author = request.form['readerName']
        password = request.form['readerPassword']
        
        flag = register_fn(author,password)
        if flag:
            return "注册成功，请登录"
        else:
            return "注册失败，用户名被占用或密码不符合"
    else:
        return render_template('reader_register.html')
    