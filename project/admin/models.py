import pymssql

def exec(s):
    database = 'NovelWebsite'
    conn = pymssql.connect(server = '127.0.0.1',port=1433,user='sa',password = '123456',database=database)
    cursor = conn.cursor()
    cursor.execute(s)
    ret = []
    row = cursor.fetchone()
    while row:
    	ret.append(row)
    	row = cursor.fetchone()
    conn.close()
    return ret

def main():
	s = 'select * from Student'
	print(exec(s))
if __name__ == '__main__':
	main()