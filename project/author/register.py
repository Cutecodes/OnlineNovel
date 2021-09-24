from .author import *
from .models import register as register_fn
@author.route('/register',methods=['POST','GET'])
def register():
    if request.method == 'POST':
        author = request.form['authorName']
        password = request.form['authorPassword']
        
        flag = register_fn(author,password)
        if flag:
            return "注册成功，请登录"
        else:
            return "注册失败，用户名被占用或密码不符合"
    else:
        return render_template('author_register.html')
    