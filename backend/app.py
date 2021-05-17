import os
from flask import Flask, jsonify, request
app = Flask(__name__)
import migrations

@app.route('/', methods=['GET'])
def main():
    #проверка на пустоту
    if bool(request.form) == False:
    	return ""
    elif request.form['command'] == "migration":
    	return migrations.main()
    else:
    	return ""

if __name__ == '__main__':
    app.run(host='0.0.0.0')