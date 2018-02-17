from flask import jsonify
from flask_restful import Resource

from src.game.game import Game, Puzzle
from src.game.actions import UpdatePuzzleAction
from src.game.queries import PuzzleExistsQuery

game = Game()

class Puzzles(Resource):
    def get(self):
        return game.get_puzzles()

    def put(self):
        puzzle = Puzzle(10,10)

        query = PuzzleExistsQuery(puzzle)
        puzzle_exists = game.perform_query(query)

        if(puzzle_exists):
            command = UpdatePuzzleAction(puzzle)
            game.act(command)
            return None, 200
        else:
            return None, 404




