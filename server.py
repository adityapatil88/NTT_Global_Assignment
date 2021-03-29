from flask import request
from implementations import connect_network_device
from flask import Flask

app = Flask(__name__)


@app.route('/Interface', methods=["GET"])
def index():

    if request.method == "GET":
        inter = request.args.get("interface")

        if inter:
            data = connect_network_device()
            data = [x for x in data if x['interface'] == inter]
        else:
            data = connect_network_device()

        if data:
            return {"data": data, "status_code": 200,  "message": "Successful"}
        else:
            return {"data": data, "status_code": 401,  "message": "No Running Config"}

    else:
        return "method not found"
