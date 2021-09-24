from .editor import *
from .models import login as login_verify
@editor.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        editor = request.form['editorName']
        password = request.form['editorPassword']

        if login_verify(editor,password):
            response = make_response(redirect(url_for('editor.editorcenter')))
            response.set_cookie('editorName',editor,max_age=3600)
            response.set_cookie('editorPassword',password,max_age=3600)
            
            return response

    else:
        return render_template('editor_login.html')