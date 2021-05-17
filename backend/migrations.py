import os
from flask import Flask, jsonify, request
import app
import psycopg2

def main():
	#подключение к бд
	db = psycopg2.connect(
		database="temperature_database",
		user="queantorium_admin",
		password="PaSsWoRd21",
		host="pg_db",
		port="5432"
	)
	
	#устанавливаем курсор
	cursor = db.cursor()

	#запускаем миграции

	#собираем список с именами файлов
	files = os.listdir("migration/")
	for file in range(len(files)):
		#сюда вносите изменения о работе отдельных миграций
		#собираем список со строками миграции
		migration = open('migration/' + files[file], 'r').readlines()
		#собираем в один файл

		result = ""
		for line in range(len(migration)):
			result += migration[line] + " "
	
		#добавляем
		cursor.execute(result)

	db.commit()

	return "Complete!"