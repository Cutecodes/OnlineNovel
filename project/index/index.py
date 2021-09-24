from flask import Blueprint,render_template,url_for,request,make_response,redirect

_index = Blueprint('index',__name__,template_folder='templates')
from .models import login as login_verify
from .models import get_novels
@_index.route('/',methods=['POST','GET'])
def index():
    
    reader = request.cookies.get('readerName')
    password = request.cookies.get('readerPassword')
    logined = login_verify(reader,password)
    novels = get_novels()
    
    if novels is not None:
        return render_template('index.html',logined=logined,novels=novels)
    else:
        novels={"玄幻":[]}
        return render_template('index.html',logined=logined,novels=novels)
    