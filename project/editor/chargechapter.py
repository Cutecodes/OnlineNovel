from .editor import *
from .models import login as login_verify
from .models import get_chapter_by_id
from .models import update_chapter_state
@editor.route('/<novelid>/<chapternum>',methods=['POST','GET'])
def chargechapter(novelid,chapternum):
    editor = request.cookies.get('editorName')
    password = request.cookies.get('editorPassword')
    
    if request.method == 'POST':
        if login_verify(editor,password):
            chapterstate = request.form['state']
            
            
            flag = update_chapter_state(novelid,chapternum,chapterstate)

            if flag:
                return '审核成功'
            else:
                return '审核失败'
        else:
            return redirect(url_for('editor.login'))
    else:
        
        if login_verify(editor,password):
            chapter,chaptercontent = get_chapter_by_id(novelid,chapternum)
            if chapter is None:
                return '打开失败'
            else:
                return render_template('editor_chapter.html',chapter=chapter,chaptercontent=chaptercontent)
        else:
            return redirect(url_for('editor.login'))


    