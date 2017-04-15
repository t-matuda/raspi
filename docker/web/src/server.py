import json
import os
import time
import pymongo
from datetime import datetime
from flask import Flask, Response, request

ip =os.getenv("MONGO_PORT_27017_TCP_ADDR", "172.17.0.2")
port =int(os.getenv("MONGO_PORT_27017_TCP_PORT", "27017"))
client = pymongo.MongoClient(ip, port)
db = client.tempdb
co = db.temperature

app = Flask(__name__, static_url_path='', static_folder='public')
app.add_url_rule('/', 'root', lambda: app.send_static_file('index.html'))

@app.route('/api/temperatures', methods=['GET', 'POST'])
def temps_handler():
    data = list(co.find({}, {'time':True, 'value':True, '_id':False}))
    times = [x['time'] for x in data]
    values = [x['value'] for x in data]
    temps = {
      'times': times,
      'values': values,
    }
    return Response(
        json.dumps(temps),
        mimetype='application/json',
        headers={
            'Cache-Control': 'no-cache',
            'Access-Control-Allow-Origin': '*'
        }
    )

@app.route('/api/latest', methods=['GET'])
def latest_handler():
    data = list(co.find({}, {'time':True, 'value':True, '_id':False}).sort('_id', pymongo.DESCENDING).limit(1))[0]
    return Response(
        json.dumps(data),
        mimetype='application/json',
        headers={
            'Cache-Control': 'no-cache',
            'Access-Control-Allow-Origin': '*'
        }
    )

@app.route('/api/comments', methods=['GET', 'POST'])
def comments_handler():
    with open('comments.json', 'r') as f:
        comments = json.loads(f.read())

    if request.method == 'POST':
        new_comment = request.form.to_dict()
        new_comment['id'] = int(time.time() * 1000)
        comments.append(new_comment)

        with open('comments.json', 'w') as f:
            f.write(json.dumps(comments, indent=4, separators=(',', ': ')))

    return Response(
        json.dumps(comments),
        mimetype='application/json',
        headers={
            'Cache-Control': 'no-cache',
            'Access-Control-Allow-Origin': '*'
        }
    )


if __name__ == '__main__':
    app.run(port=5000, debug=True, host='172.17.0.4')
