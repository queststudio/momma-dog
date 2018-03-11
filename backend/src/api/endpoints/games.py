from flask_restful import Resource, request

from src.game.store import store, init_state
from src.game.actions import RestartAction
from src.game.queries import GameQuery


class CurrentGame(Resource):
    def get(self):
        query = GameQuery()
        current_game = store.perform_query(query)
        result = {
            'game': current_game
        }
        return result, 200


    def post(self):
        action = RestartAction(init_state)
        store.act(action)

        #ToDo decide if I really need this part here
        query = GameQuery()
        current_game = store.perform_query(query)
        result = {
            'game': current_game
        }

        return result, 200
