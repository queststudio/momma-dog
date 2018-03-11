from flask_restful import Resource, request

from src.game.store import init_state
from src.game.actions import RestartAction
from src.game.queries import GameQuery


class CurrentGame(Resource):
    def __init__(self, store):
        self.store = store

    def get(self):
        query = GameQuery()
        current_game = self.store.perform_query(query)
        result = {
            'game': current_game
        }
        return result, 200

    def post(self):
        action = RestartAction(init_state)
        self.store.act(action)

        # ToDo decide if I really need this part here
        query = GameQuery()
        current_game = self.store.perform_query(query)
        result = {
            'game': current_game
        }

        return result, 200
