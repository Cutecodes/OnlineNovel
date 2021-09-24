from .author import *
from .models import login as login_verify
from .models import get_novel_by_author
@author.route('/authornovel',methods=['POST','GET'])
def authornovel():
    author = request.cookies.get('authorName')
    password = request.cookies.get('authorPassword')
    if login_verify(author,password):
        novel = get_novel_by_author(author)
        return render_template('author_novel.html',novel=novel)
    else:
        return redirect(url_for('author.login'))
    