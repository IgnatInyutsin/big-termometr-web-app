import os
import app
import database 
import time
from flask import jsonify

def main(data):
	# Подключаемся к БД
	db = database.init()

	#устанавливаю курсор
	cursor = db.cursor()
	
	#запрос
	cursor.execute('''SELECT temperature.*, people."name", people.lastname 
	FROM temperature
	LEFT JOIN people ON people.id=user_id''')
	
	result=cursor.fetchall()
	
	return {"data":result}
