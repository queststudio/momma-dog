from flask import jsonify
from flask_restful import Resource
import json

from src.game.queries import LocksQuery


class Locks(Resource):
    def __init__(self, store):
        self.store = store

    def get(self):
        query = LocksQuery()
        locks = self.store.perform_query(query)

        result = {
            'locks': [lock.serialize() for lock in locks]
        }
        return result, 200
