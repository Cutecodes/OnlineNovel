from .author import *
from .models import login as login_verify
from .models import get_author
@author.route('/authorcenter',methods=['POST','GET'])
def authorcenter():
    author = request.cookies.get('authorName')
    password = request.cookies.get('authorPassword')
    if login_verify(author,password):
        author = get_author(author)
        return render_template('author_center.html',author=author)
    else:
        return redirect(url_for('author.register'))
    