import pymysql
from core.pyProperties import parse

conn = None

def setConnectionData(data):
	global conn
	if conn != None:
		return
	datas = parse(data)
	conn = pymysql.connect(datas.get("db.host"),datas.get("db.username"),datas.get("db.password"),datas.get("db.database"))


def execute(sql):
	try:
		cursor = conn.cursor()
		cursor.execute(sql)
		return cursor.fetchall()
	except Exception as e:
		conn.rollback()
		close()
		raise e
	
def close():
	conn.close()