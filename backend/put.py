import os
import app
import psycopg2
import time

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
	#добавляю ячейку
	cursor.execute('''INSERT INTO temperature (user_id, temperature, datatime) 
	VALUES (${data.user_id}, ${data.temperature}, ${int(time.time())});''')	
	#отправляем изменения
	db.commit()

	return "Complete!"