from flask import jsonify
from flask_restful import Resource

healthy = {
    'status': 'healthy'
}

class Health(Resource):
    def get(self):
        return jsonify(healthy)