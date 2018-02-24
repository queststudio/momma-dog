from flask_restful import Resource, request

from src.game.game import game
from src.game.models import Puzzle, PuzzleState
from src.game.actions import UpdatePuzzleAction
from src.game.queries import ReporterExistsQuery

class Reporters(Resource):
    def put(self, reporter: str):
        devices = request.json.get('devices')

        if not devices:
            return 400

        query = ReporterExistsQuery(reporter)
        reporter_exists = game.perform_query(query)
        if not reporter_exists:
            return None, 404

        for device in devices:
            puzzle = Puzzle(reporter, device['address'])
            puzzle.state = PuzzleState(device['state'])
            command = UpdatePuzzleAction(puzzle)
            game.act(command)

        return None, 200
