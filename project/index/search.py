from flask import Blueprint,render_template,url_for,request,make_response,redirect
from .index import *
from .index import _index
from .models import login as login_verify
from .models import search_novels
@_index.route('/search',methods=['POST','GET'])
def search():
    if request.method == 'POST':
        keyword = request.form['searchContent']
    else:
        keyword = request.args['searchContent']    
        
        novels = search_novels(keyword)
        return render_template('search.html',novels=novels)
    
    
    