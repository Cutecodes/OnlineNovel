from .author import *
from .models import login as login_verify
from .models import create_chapter

@author.route('/<novel_id>/createchapter',methods=['POST','GET'])
def createchapter(novel_id):
    author = request.cookies.get('authorName')
    password = request.cookies.get('authorPassword')
    if request.method == 'POST':
        if login_verify(author,password):
            chaptertype = request.form['type']
            chaptername = request.form['txtTitle']
            
            
            chaptercontnet = request.form['content']
            
            flag = create_chapter(novel_id,chaptername,chaptertype,chaptercontnet)

            if flag:
                return '创建章节成功'
            else:
                return '创建章节失败'
    else:
        
        if login_verify(author,password):
            return render_template('author_createchapter.html',novel_id=novel_id)
        else:
            return redirect(url_for('author.login'))