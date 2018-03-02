from flask_restful import Resource, request

from src.game.game import game, init_state
from src.game.actions import RestartAction
from src.game.queries import GameQuery
from src.relays.restart import restart


class CurrentGame(Resource):
    def get(self):
        query = GameQuery()
        current_game = game.perform_query(query)
        result = {
            'game': current_game
        }
        return result, 200


    def post(self):
        action = RestartAction(init_state)
        game.act(action)

        query = GameQuery()
        current_game = game.perform_query(query)
        result = {
            'game': current_game
        }

        restart() #ToDo Move that to some kind of middleware or any other better place for the side effects

        return result, 200
