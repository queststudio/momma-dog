from flask import jsonify
from flask_restful import Resource, request
import json

from src.game.game import game
from src.game.models import Puzzle, PuzzleState
from src.game.actions import UpdatePuzzleAction
from src.game.queries import PuzzleExistsQuery, PuzzleQuery


class Puzzles(Resource):
    def get(self):
        puzzles = game.get_puzzles()
        result = {
            'puzzles': [puzzle.serialize() for puzzle in puzzles]
        }
        return result, 200


class ReporterPuzzles(Resource):
    def get(self, reporter_id: int, puzzle_id: int):
        puzzle = Puzzle(reporter_id, puzzle_id)
        query = PuzzleQuery(puzzle)
        puzzle = game.perform_query(query)

        if (puzzle):
            return puzzle.serialize(), 200
        else:
            return None, 404

    def put(self, reporter_id: int, puzzle_id: int):
        puzzle = Puzzle(reporter_id, puzzle_id)
        new_state = request.json.get('state')

        if not new_state:
            return 401

        puzzle.state = PuzzleState(new_state)


        query = PuzzleExistsQuery(puzzle)
        puzzle_exists = game.perform_query(query)

        if (puzzle_exists):
            command = UpdatePuzzleAction(puzzle)
            game.act(command)
            return None, 200
        else:
            return None, 404
