from copy import deepcopy
from src.game.models import State, Puzzle


class Query:
    def perform(self, state: State):
        return deepcopy(state)


class PuzzleExistsQuery(Query):
    def __init__(self, puzzle: Puzzle):
        self.puzzle = puzzle

    def perform(self, state: State):
        for lock in state.locks:
            for puzzle in lock.puzzles:
                if(puzzle.reporter==self.puzzle.reporter
                    and puzzle.local_address == self.puzzle.local_address):
                    return True

        return False
