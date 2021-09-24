from .author import *
from .models import login as login_verify
from .models import get_chapter_by_novelid
@author.route('/<novel_id>',methods=['POST','GET'])
def authorchapter(novel_id):
    author = request.cookies.get('authorName')
    password = request.cookies.get('authorPassword')
    if login_verify(author,password):
        chapter = get_chapter_by_novelid(novel_id)
        return render_template('author_chapter.html',chapters=chapter,novel_id=novel_id)
    else:
        return redirect(url_for('author.login'))
    