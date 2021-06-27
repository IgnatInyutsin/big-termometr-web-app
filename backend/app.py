import os
from flask import Flask, jsonify, request, Response
import migrations
import put
import siteDatabasePull
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    #проверка на пустоту
    if bool(request.form) == False:
    	respData = ""
    elif request.form['command'] == "migration":
    	respData = migrations.main()
    elif request.form['command'] == "put":
    	respData = put.main(request.form)
    elif request.form['command'] == "site-database-pull":
        respData = str(siteDatabasePull.main(request.form))
    else:
        respData = ""
    	
    resp = Response(respData)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Content-Type'] = 'application/json'
    return resp

if __name__ == '__main__':
    app.run(host='0.0.0.0')