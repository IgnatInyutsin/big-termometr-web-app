import os
from flask import Flask, jsonify, request, Response
import migrations
import put
import siteDatabasePull
import json

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def main():
    #проверка на пустоту
    if bool(request.args) == False:
    	respData = False
    elif request.args['command'] == "migration":
    	respData = migrations.main()
    elif request.args['command'] == "put":
    	respData = put.main(request.form)
    elif request.args['command'] == "site-database-pull":
        respData = siteDatabasePull.main(request.form)
    else:
        respData = False 

    resp = Response(json.dumps(respData, sort_keys=True, indent=2, ensure_ascii=False, default=str))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Content-Type'] = 'application/json'
    return resp



if __name__ == '__main__':
    app.run(host='0.0.0.0')
