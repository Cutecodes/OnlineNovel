from .author import *
from .models import login as login_verify
from .models import create_novel
@author.route('/createnovel',methods=['POST','GET'])
def createnovel():
    author = request.cookies.get('authorName')
    password = request.cookies.get('authorPassword')
    if request.method == 'POST':
        if login_verify(author,password):
            noveltype = request.form['type']
            noveltitle = request.form['title']
            
            novelcover = request.files['cover']
            
            novelcontnet = request.form['contens']
            
            flag = create_novel(author,noveltitle,noveltype,novelcover,novelcontnet)
            if flag:
                return '创建小说成功'
            else:
                return '创建小说失败'
    else:
        
        if login_verify(author,password):
            return render_template('author_createnovel.html')
        else:
            return redirect(url_for('author.login'))