import os
from flask import Flask
from flask import request
from flask import make_response

import json
import psycopg2
app = Flask(__name__)


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
    if req.get("queryResult").get("action") != "Temperature":
       return {}
    result = req.get("queryResult")
    parameters = result.get("parameters")
    city = parameters.get("city")
      
    print(city)
    conn = psycopg2.connect(database = "exam", user = "postgres", password = "1234", host = "localhost", port = "5432")
    print "Opened database successfully"

    cur = conn.cursor()
    sql="SELECT TEMPERATURE FROM WEATHER WHERE city='%s'"%city
    cur.execute(sql)
    
    print "Operation done successfully";
    record = cur.fetchone()
    print(record)
    temp=str(record[0])
    print(record,record[0])
    speech="The temperature in " + city + " is " + temp 
    conn.close()

    return {
        'fulfillmentText':speech,
        'displayText':speech,
        'source':'dialogflow'
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=True, port=port, host='0.0.0.0')
