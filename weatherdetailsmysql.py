
from flask import Flask
from flask import request
from flask import make_response

import json
import MySQLdb
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'
@app.route('/webhook',methods=['POST'])
def webhook():
    req = request.get_json(silent=True,force=True)
    print(json.dumps(req,indent=4))
    res = webHookResult(req)
    res = json.dumps(res,indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-type'] = 'application/json'
    return r

def webHookResult(req): 
    if req.get("queryResult").get("action") != "weather":
       return {}
    result = req.get("queryResult")
    parameters = result.get("parameters")
    zone = parameters.get("geo-city")
   
    
    db = MySQLdb.connect(host='localhost',
                    database='db',
                    user='root',
                    password='1234',
                    )
    sql="SELECT temperature FROM WEATHER WHERE city='%s'"%zone
    cursor =db.cursor()
    cursor.execute(sql)
    record = cursor.fetchone()
    temp=str(record[0])
    print(record,record[0])
    speech="The temperature in " + zone + " is " + temp 
    return {
        'fulfillmentText':speech,
        'displayText':speech,
        'source':'dialogflow'
    }






if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=True, port=port, host='0.0.0.0')


