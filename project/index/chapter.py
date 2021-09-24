from .models import login as login_verify
from .models import get_novels_by_id
from .models import get_chapter
from .index import _index
from .models import check_chapter
from .models import subcribe_chapter
from .index import *
@_index.route('/<novelid>/<chapternum>',methods=['POST','GET'])
def chapter(novelid,chapternum):

    reader = request.cookies.get('readerName')
    password = request.cookies.get('readerPassword')
    lastchapter = ()
    nextchapter = ()
    chapter = ()
    chaptercontent = None
    if check_chapter(reader,novelid,chapternum):
        lastchapter,nextchapter,chapter,chaptercontent = get_chapter(novelid,chapternum)
    else:
        lastchapter,nextchapter,chapter,_ = get_chapter(novelid,chapternum)

    
    return render_template('chapter.html',lastchapter=lastchapter,nextchapter=nextchapter,chapter=chapter,chaptercontent=chaptercontent)
    

@_index.route('/<novelid>/<chapternum>/subscribe',methods=['POST','GET'])
def subcribe(novelid,chapternum):
    if request.method == 'GET':
        reader = request.cookies.get('readerName')
        password = request.cookies.get('readerPassword')
        if login_verify(reader,password):
            if subcribe_chapter(reader,novelid,chapternum):
                return "购买成功"

        return "购买失败，请检查余额"


    else:
        pass

