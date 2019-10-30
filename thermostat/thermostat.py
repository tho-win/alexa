#!flask/bin/python
from flask import Flask, jsonify, abort, make_response, request

app = Flask(__name__)

current_temp = 75
current_setpoint = 75

@app.route('/governor/api/v1.0/current-temp', methods=['GET'])
def get_current_temp():
    return jsonify({'current-temp': current_temp})

@app.route('/governor/api/v1.0/current-setpoint', methods=['GET'])
def get_current_setpoint():
    return jsonify({'current-setpoint': current_setpoint})

@app.errorhandler(404)
def not_found(error):
        return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/governor/api/v1.0/current-setpoint', methods=['PUT'])
def set_setpoint():
        print(request.json)
        global current_setpoint
        current_setpoint = request.json.get('setpoint')
        return jsonify({'current_setpoint': current_setpoint})

if __name__ == '__main__':
    app.run(host="0.0.0.0")