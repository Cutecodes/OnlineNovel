from flask import Blueprint,render_template,url_for,request,make_response,redirect
from .models import exec
_admin = Blueprint('admin',__name__,template_folder='templates')

@_admin.route('/')
def admin():
    user = request.cookies.get('user')
    password = request.cookies.get('password')
    if user=='admin' and password == '123456':
        return render_template('admin.html')
    else:
        return render_template('admin_login.html')

@_admin.route('/model',methods=['POST'])
def model():
    s = request.get_data('content')
    r = exec(s)
    re = ""
    for item in r:
        for items in item:
            re = re +' '+ str(items)
        re = re + '\n'
    return re
@_admin.route('/login',methods=['POST','GET'])
def admin_login():
    if request.method == 'POST':
        user = request.form['u']
        password = request.form['p']
        if user=='admin' and password == '123456':
            response = make_response(redirect(url_for('admin.admin')))
            response.set_cookie('user',user,max_age=3600)
            response.set_cookie('password',password,max_age=3600)
            
            return response
        else:
            return "登录失败，请检查账户密码"
    else:
        return render_template('admin_login.html')



