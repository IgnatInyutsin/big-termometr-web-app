import os
import app
import psycopg2
import time
from flask import jsonify

def main(data):
	#подключение к бд
	db = psycopg2.connect(
		database="temperature_database",
		user="queantorium_admin",
		password="PaSsWoRd21",
		host="pg_db",
		port="5432"
	)
	#устанавливаю курсор
	cursor = db.cursor()
	
	#запрос
	cursor.execute('''SELECT temperature.*, people."name", people.lastname 
	FROM temperature
	JOIN people ON people.id=user_id''')
	
	result=cursor.fetchall()
	
	return {"data":result}
