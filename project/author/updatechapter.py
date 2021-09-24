from .author import *
from .models import login as login_verify
from .models import update_chapter
from .models import get_chapter_by_id

@author.route('/<novel_id>/<chapternum>',methods=['POST','GET'])
def updatechapter(novel_id,chapternum):
    author = request.cookies.get('authorName')
    password = request.cookies.get('authorPassword')
    if request.method == 'POST':
        if login_verify(author,password):
            chaptertype = request.form['type']
            chaptername = request.form['txtTitle']
            
            
            chaptercontnet = request.form['content']
            
            flag = update_chapter(novel_id,chapternum,chaptername,chaptertype,chaptercontnet)

            if flag:
                return '修改章节成功'
            else:
                return '修改章节失败'
    else:
        
        if login_verify(author,password):
            chapter,chaptercontnet = get_chapter_by_id(novel_id,chapternum)
            if chapter is not None:
                return render_template('author_updatechapter.html',chapter=chapter,chaptercontent=chaptercontnet)
            else:
                return '没有此章节'

        else:
            return redirect(url_for('author.login'))