from flask import jsonify
from flask_restful import Resource

from src.game.game import game


class Locks(Resource):
    def get(self):
        return game.get_locks(), 200
