from .models import login as login_verify
from .models import get_novels_by_id
from .index import _index
from .index import *
from .models import add_bookshelf
@_index.route('/<int:novelid>',methods=['POST','GET'])
def novel(novelid):

    reader = request.cookies.get('readerName')
    password = request.cookies.get('readerPassword')

    novel,chapters = get_novels_by_id(novelid)
    
    return render_template('novel.html',novel=novel,chapters=chapters)
    

@_index.route('/<novelid>/cover',methods=['POST','GET'])
def novelcover(novelid):
    if request.method == 'GET':
        if novelid is None:
            pass
        else:
            NOVEL_FOLDER = './database/novel/'
            
            
            image_data = open(NOVEL_FOLDER+novelid+'/'+'cover', "rb").read()
            if len(image_data)==0:
                image_data = open("./static/images/nocover.jpg","rb").read()
            response = make_response(image_data)
            response.headers['Content-Type'] = 'image/jpg'
            return response
            
    else:
        pass

@_index.route('/<novelid>/addbookshelf',methods=['POST','GET'])
def addbookshelf(novelid):
    if request.method == 'GET':
        reader = request.cookies.get('readerName')
        password = request.cookies.get('readerPassword')
        if login_verify(reader,password):
            if add_bookshelf(reader,novelid):
                return "已加入书架"

        return "加入失败"


    else:
        pass


