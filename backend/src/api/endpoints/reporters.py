from flask_restful import Resource, request

from src.game.models import Puzzle, PuzzleState
from src.game.actions import UpdatePuzzleAction
from src.game.queries import ReporterExistsQuery


class Reporters(Resource):
    def __init__(self, store):
        self.store = store

    def put(self, reporter: str):
        devices = request.json.get('devices')

        if not devices:
            return 400

        print('[{}] {}'.format(reporter, devices))  # ToDo use logger

        query = ReporterExistsQuery(reporter)
        reporter_exists = self.store.perform_query(query)
        if not reporter_exists:
            return None, 404

        for device in devices:
            puzzle = Puzzle(reporter, device['address'])
            puzzle.state = PuzzleState(device['state'])
            command = UpdatePuzzleAction(puzzle)
            self.store.act(command)

        return None, 200
