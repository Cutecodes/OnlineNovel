from .editor import *
from .models import login as login_verify
from .models import get_editor
@editor.route('/editorcenter',methods=['POST','GET'])
def editorcenter():
    editor = request.cookies.get('editorName')
    password = request.cookies.get('editorPassword')
    if login_verify(editor,password):
        editor = get_editor(editor)
        return render_template('editor_center.html',editor=editor)
    else:
        return render_template('editor_login.html')

@editor.route('/',methods=['POST','GET'])
def index():
    return redirect(url_for('editor.editorcenter'))
    