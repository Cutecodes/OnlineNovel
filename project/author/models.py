from DBUtils.PersistentDB import PersistentDB
import pymssql
import os
POOL = PersistentDB(
    creator=pymssql,  # 使用链接数据库的模块
    maxusage=None,  # 一个链接最多被重复使用的次数，None表示无限制
    setsession=[],  # 开始会话前执行的命令列表。如：["set datestyle to ...", "set time zone ..."]
    ping=0,
    # ping MySQL服务端，检查是否服务可用。# 如：0 = None = never, 1 = default = whenever it is requested, 2 = when a cursor is created, 4 = when a query is executed, 7 = always
    closeable=False,
    # 如果为False时， conn.close() 实际上被忽略，供下次使用，再线程关闭时，才会自动关闭链接。如果为True时， conn.close()则关闭链接，那么再次调用pool.connection时就会报错，因为已经真的关闭了连接（pool.steady_connection()可以获取一个新的链接）
    threadlocal=None,  # 本线程独享值得对象，用于保存链接对象，如果链接对象被重置
    host='127.0.0.1',
    port=1433,
    user='sa',
    password='123456',
    database='NovelWebsite',
    charset='utf8'
)
NOVEL_FOLDER = './database/novel/'

def register(id,password):
    conn = POOL.connection()
    cursor = conn.cursor()
    ret = True   
    try:       
        cursor.execute('insert into AUTHOR(AuthorID,Points,AuthorPassWord) values(%s,0,%s)',(id,password))
        cursor.execute("insert into IN_CHARGE_OF(EditorID,AuthorID) values('0',%s)",id)
        

        conn.commit()
    except Exception as e:
        print(e)
        ret = False
    finally:
        cursor.close()
        conn.close()
    return ret

def login(id,password):
    conn = POOL.connection()
    cursor = conn.cursor()
    ret = False 
    really_password = None  
    try:       
        cursor.execute('select AuthorPassWord from AUTHOR where AuthorID=%s',(id))
        really_password = cursor.fetchone()
        conn.commit()
    except Exception as e:

        ret = False
    finally:

        
        if really_password is not None and really_password[0]==password:
            ret = True
        cursor.close()
        conn.close()
    return ret

def get_author(id):
    conn = POOL.connection()
    cursor = conn.cursor()
    user = None  
    try:       
        cursor.execute('select * from AUTHOR where AuthorID=%s',(id))
        user = cursor.fetchone()
        conn.commit()
    except Exception as e:
        user = None
    finally:
        cursor.close()
        conn.close()
    return user

def create_novel(author,name,noveltype,cover,profile):
    conn = POOL.connection()
    cursor = conn.cursor()
    ret = False  
    
    try:       
        cursor.execute("insert into NOVEL(NovelName,AuthorID,NovelType,NovelState,NovelProfile) values(%s,%s,%s,'连载',%s)",(name,author,noveltype,profile))
        cursor.execute('select @@identity')
        novelid = cursor.fetchone()
        os.mkdir(NOVEL_FOLDER+str(novelid[0]))
        filepath = NOVEL_FOLDER+str(novelid[0])+'/cover'
        cover.save(filepath)
        conn.commit()
        ret = True
    except Exception as e:

        print(e)
        ret = False
    finally:
        cursor.close()
        conn.close()
    return ret

def get_novel_by_author(author):
    conn = POOL.connection()
    cursor = conn.cursor()
    novel = None  
    
    try:       
        cursor.execute('select * from NOVEL where AuthorID=%s',(author))
        novel = cursor.fetchall()
        conn.commit()
    except Exception as e:
        print(e)
        novel = None
    finally:
        cursor.close()
        conn.close()
    return novel

def get_chapter_by_novelid(novelid):
    conn = POOL.connection()
    cursor = conn.cursor()
    chapter = None  
    
    try:       
        cursor.execute('select * from CHAPTER where NovelID=%s',(novelid))
        chapter = cursor.fetchall()
        conn.commit()
    except Exception as e:
        print(e)
        novel = None
    finally:
        cursor.close()
        conn.close()
    return chapter

def create_chapter(novelid,chaptername,chaptertype,chaptercontent):
    conn = POOL.connection()
    cursor = conn.cursor()
    ret = False  
    
    try:       
        cursor.execute("insert into CHAPTER(NovelID,ChapterName,ChapterType,ChapterState) values(%s,%s,%s,'审核中')",(novelid,chaptername,chaptertype))
        cursor.execute('select @@identity')
        chaperid = cursor.fetchone()
        
        filepath = NOVEL_FOLDER+novelid+'/'+str(chaperid[0])
        f = open(filepath,'w',encoding="utf-8")
        f.write(chaptercontent)
        f.close()
        conn.commit()
        ret = True
    except Exception as e:

        print(e)
        ret = False
    finally:
        cursor.close()
        conn.close()
    return ret

def get_chapter_by_id(novel_id,chapternum):
    conn = POOL.connection()
    cursor = conn.cursor()
    chapter = None 
    chaptercontent = None
    try:       
        cursor.execute("select *from CHAPTER where NovelID=%s and ChapterNum=%s ",(novel_id,chapternum))
        chapter = cursor.fetchone()
        
        filepath = NOVEL_FOLDER+novel_id+'/'+chapternum
        f = open(filepath,'r',encoding="utf-8")
        
        chaptercontent = f.read()

        f.close()
        conn.commit()
        
    except Exception as e:

        print(e)
        chapter=None
    finally:
        cursor.close()
        conn.close()
    return chapter,chaptercontent

def update_chapter(novel_id,chapternum,chaptername,chaptertype,chaptercontnet):
    conn = POOL.connection()
    cursor = conn.cursor()
    ret = False  
    
    try:       
        cursor.execute("update CHAPTER set ChapterName=%s,ChapterType=%s,ChapterState='审核中' where NovelID=%s and ChapterNum=%s",(chaptername,chaptertype,novel_id,chapternum))
        
        filepath = NOVEL_FOLDER+novel_id+'/'+chapternum
        f = open(filepath,'w',encoding="utf-8")
        f.write(chaptercontnet)
        f.close()
        conn.commit()
        ret = True
    except Exception as e:

        print(e)
        ret = False
    finally:
        cursor.close()
        conn.close()
    return ret

def main():
    s=create_chapter('1','test',0,'dfhdjhfjd')
    
    print(s)
if __name__ == '__main__':
	main()