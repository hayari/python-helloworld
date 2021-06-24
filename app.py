from flask import Flask,make_response
import json 
import logging
curr_metric={"usercount": 0, "usercountactive": 0}
FORMAT= "%(asctime)s, %(message)s endpoint was reached"
logging.basicConfig(
    filename="app.log",
    format=FORMAT,
    style="{",
    level="DEBUG"
)

logger = logging.getLogger('app')
app = Flask(__name__)


@app.route("/")
def hello():
    app.logger.info("/")
    
    curr_metric["usercount"] +=1
    curr_metric["usercountactive"] +=1
    return "Hello World!"

@app.route("/status")
def status():
    app.logger.info('/status')
    response = make_response(json.dumps({"result": "OK - healthy"}))
    response.status_code = 200
    response.mimetype='application/json'
    return response

@app.route("/metrics")
def metrics():
    app.logger.info('/metrics')
    response = make_response(json.dumps({"data": curr_metric, "code": 0, "status": "success"}))
    response.status_code = 200
    response.mimetype='application/json'
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
