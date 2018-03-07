from flask_restful import Resource, request

from src.game.store import store
from src.game.models import Puzzle, PuzzleState
from src.game.actions import UpdatePuzzleAction
from src.game.queries import PuzzleExistsQuery, PuzzleQuery, PuzzlesQuery


class Puzzles(Resource):
    def get(self):
        query = PuzzlesQuery()
        puzzles = store.perform_query(query)

        result = {
            'puzzles': [puzzle.serialize() for puzzle in puzzles]
        }
        return result, 200


class ReporterPuzzles(Resource):
    def get(self, reporter: int, local_address: int):
        puzzle = Puzzle(reporter, local_address)
        query = PuzzleQuery(puzzle)
        puzzle = store.perform_query(query)

        if (puzzle):
            return puzzle.serialize(), 200
        else:
            return None, 404

    def put(self, reporter: str, local_address: int):
        puzzle = Puzzle(reporter, local_address)
        new_state = request.json.get('state')

        if not new_state:
            return 400

        puzzle.state = PuzzleState(new_state)


        query = PuzzleExistsQuery(puzzle)
        puzzle_exists = store.perform_query(query)

        if (puzzle_exists):
            command = UpdatePuzzleAction(puzzle)
            store.act(command)
            return None, 200
        else:
            return None, 404
