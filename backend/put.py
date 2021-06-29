import os
import app
import database 
import time

def main(data):

	# Подключаемся к БД
	db = database.init()

	#устанавливаю курсор
	cursor = db.cursor()
	#добавляю ячейку
	cursor.execute("""INSERT INTO temperature (user_id, temperature, datatime) 
	VALUES (%s, %s, %s);""",(data["user_id"], data["temperature"], int(time.time())))	
	#отправляем изменения
	db.commit()

	return "Complete!"
