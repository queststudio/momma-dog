from flask_restful import Resource, request

from src.game.store import store
from src.game.models import SwitchState, Switch as SwitchModel
from src.game.actions import UpdateSwitchAction
from src.game.queries import SwitchesQuery, SwitchExistsQuery


class Switches(Resource):
    def get(self):
        query = SwitchesQuery()
        switches = store.perform_query(query)
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
        switch_exists = store.perform_query(query)

        if (switch_exists):
            command = UpdateSwitchAction(id, SwitchState(new_state))
            store.act(command)
            return None, 200
        else:
            return None, 404
