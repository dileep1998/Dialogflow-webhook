# To get static reply from webhook

import urllib
import json


from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)




@app.route('/static_reply', methods=['POST'])
def static_reply():
    speech = "Hello there, this reply is from the webhook !! "
    string = "Weather here is Good !! There is a sudden change in weather"
    Message = "this is the message from webhook"

    output = {

        "fulfillmentText": string,
        "source": string
    }

    res = json.dumps(output, indent=4)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print ("Starting app on port %d" %(port))

    app.run(debug=True, port=port, host='0.0.0.0')


