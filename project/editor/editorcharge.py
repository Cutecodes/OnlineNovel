from .editor import *
from .models import login as login_verify
from .models import get_chapters_by_editor
@editor.route('/editorcharge',methods=['POST','GET'])
def editorcharge():
    editor = request.cookies.get('editorName')
    password = request.cookies.get('editorPassword')
    if login_verify(editor,password):
        chapters = get_chapters_by_editor(editor)

        return render_template('editor_charge.html',chapters=chapters)
    else:
        return render_template('editor_login.html')


    