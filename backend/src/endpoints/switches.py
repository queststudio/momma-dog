from flask_restful import Resource, request

from src.game.game import game
from src.game.models import SwitchState, Switch as SwitchModel
from src.game.actions import UpdateSwitchAction
from src.game.queries import SwitchesQuery, SwitchExistsQuery


class Switches(Resource):
    def get(self):
        query = SwitchesQuery()
        switches = game.perform_query(query)
        result = {
            'switches': [switch.serialize() for switch in switches]
        }
        return result, 200


class Switch(Resource):
    def put(self, id: int):
        new_state = request.json.get('state')
        if not new_state:
            return 400

        query = SwitchExistsQuery(id)
        switch_exists = game.perform_query(query)

        if (switch_exists):
            command = UpdateSwitchAction(id, SwitchState(new_state))
            game.act(command)
            return None, 200
        else:
            return None, 404
