from .author import *
from .models import login as login_verify
@author.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        author = request.form['authorName']
        password = request.form['authorPassword']
        if login_verify(author,password):
            response = make_response(redirect(url_for('author.authorcenter')))
            response.set_cookie('authorName',author,max_age=3600)
            response.set_cookie('authorPassword',password,max_age=3600)
            
            return response
        else:
            return "failed"

    else:
        return render_template('author_login.html')