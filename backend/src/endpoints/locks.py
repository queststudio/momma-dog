from flask import jsonify
from flask_restful import Resource
import json

from src.game.store import store
from src.game.queries import LocksQuery


class Locks(Resource):
    def get(self):
        query = LocksQuery()
        locks = store.perform_query(query)

        result = {
            'locks': [lock.serialize() for lock in locks]
        }
        return result, 200
