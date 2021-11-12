import pysql
from app import app
from config import sql
from flask import jsonify
from flask import flash, request
		
@app.route('/add', methods=['POST'])
def add_emp():
	try:
		_json = request.json
		_type = _json['type']
		_title = _json['title']	
		if _type and _title and request.method == 'POST':			
			sqlQuery = "INSERT INTO testdata(type, title) VALUES(%s, %s)"
			bindData = (_type, _title)
			conn = sql.connect()
			cursor = conn.cursor()
			cursor.execute(sqlQuery, bindData)
			conn.commit()
			respone = jsonify('Employee added successfully!')
			respone.status_code = 200
			return respone
		else:
			return not_found()
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		
@app.route('/test')
def emp():
	try:
		conn = sql.connect()
		cursor = conn.cursor(pysql.cursors.DictCursor)
		cursor.execute("SELECT id, type, title FROM testdata")
		empRows = cursor.fetchall()
		respone = jsonify(empRows)
		respone.status_code = 200
		return respone
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		
@app.route('/test/<int:id>')
def emp(id):
	try:
		conn = sql.connect()
		cursor = conn.cursor(pysql.cursors.DictCursor)
		cursor.execute("SELECT id, type, title FROM testdata WHERE id =%s", id)
		empRow = cursor.fetchone()
		respone = jsonify(empRow)
		respone.status_code = 200
		return respone
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()