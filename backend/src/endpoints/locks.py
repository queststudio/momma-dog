from flask import jsonify
from flask_restful import Resource
import json

from src.game.game import game


class Locks(Resource):
    def get(self):
        locks = game.get_locks()
        result = {
            'locks': [lock.serialize() for lock in locks]
        }
        return result, 200
