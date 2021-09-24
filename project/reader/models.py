from DBUtils.PersistentDB import PersistentDB
import pymssql
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

def register(id,password):
    conn = POOL.connection()
    cursor = conn.cursor()
    ret = True   
    try:       
        cursor.execute('insert into READER(ReaderID,Points,ReaderPassWord) values(%s,100,%s)',(id,password))

        conn.commit()
    except Exception as e:
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
        cursor.execute('select ReaderPassWord from READER where ReaderID=%s',(id))
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

def get_reader(id):
    conn = POOL.connection()
    cursor = conn.cursor() 
    user = None  
    try:       
        cursor.execute('select * from READER where ReaderID=%s',(id))
        user = cursor.fetchone()
        conn.commit()
    except Exception as e:
        user = None
    finally:
        cursor.close()
        conn.close()
    return user

def get_novels():
    conn = POOL.connection()
    cursor = conn.cursor() 
    novels = None  
    try:
        cursor.execute('select distinct NovelType from NOVEL ')
        noveltype = cursor.fetchall()
        novels = {}
        for t in noveltype:
           novels[t[0]]=[]       
        cursor.execute('select * from NOVEL order by NovelType')
        novellist = cursor.fetchall()
        for novel in novellist:
            novels[novel[3]].append(novel)

        conn.commit()
    except Exception as e:
        print(e)
        novels = None
    finally:
        cursor.close()
        conn.close()
    
    return novels

def get_subscribe(reader):
    conn = POOL.connection()
    cursor = conn.cursor() 
    chapters = ()  
    try:
        cursor.execute('select * from CHAPTER where ChapterNum in (select ChapterNum from SUBSCRIBE where ReaderID=%s )',(reader))
        chapters = cursor.fetchall()
        

        conn.commit()
    except Exception as e:
        print(e)
        
    finally:
        cursor.close()
        conn.close()
    
    return chapters

def get_bookshelf(reader):
    conn = POOL.connection()
    cursor = conn.cursor() 
    novels = ()  
    try:
        cursor.execute('select * from NOVEL where NovelID in (select NovelID from COLLECTIONS where ReaderID=%s )',(reader))
        novels = cursor.fetchall()
        

        conn.commit()
    except Exception as e:
        print(e)
        
    finally:
        cursor.close()
        conn.close()
    
    return novels

def main():
    s=login("fffffff","12456")
    print(s)
if __name__ == '__main__':
	main()