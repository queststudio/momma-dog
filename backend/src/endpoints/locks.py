from flask import jsonify
from flask_restful import Resource

from src.game.game import Game


class Locks(Resource):
    def get(self):
        return {}

