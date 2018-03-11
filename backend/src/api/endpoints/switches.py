from flask_restful import Resource, request

from src.game.models import SwitchState, Switch as SwitchModel
from src.game.actions import UpdateSwitchAction
from src.game.queries import SwitchesQuery, SwitchExistsQuery


class Switches(Resource):
    def __init__(self, store):
        self.store = store

    def get(self):
        query = SwitchesQuery()
        switches = self.store.perform_query(query)
        result = {
            'switches': [switch.serialize() for switch in switches]
        }
        return result, 200


class Switch(Resource):
    def __init__(self, store):
        self.store = store

    def put(self, id: int):
        new_state = request.json.get('state')
        if not new_state:
            return 400

        query = SwitchExistsQuery(id)
        switch_exists = self.store.perform_query(query)

        if (switch_exists):
            command = UpdateSwitchAction(id, SwitchState(new_state))
            self.store.act(command)
            return None, 200
        else:
            return None, 404
