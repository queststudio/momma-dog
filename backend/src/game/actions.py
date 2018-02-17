from copy import deepcopy
from src.game.models import State, Puzzle


class Action:
    def act(self, state: State):
        return deepcopy(state)


class UpdatePuzzleAction(Action):
    def __init__(self, puzzle: Puzzle):
        self.puzzle = puzzle

    def act(self, state: State):
        new_state = deepcopy(state)
        for lock in new_state.locks:
            for puzzle in lock.puzzles:
                if (puzzle.reporter == self.puzzle.reporter
                    and puzzle.local_address == self.puzzle.local_address):
                    puzzle.state = self.puzzle.state

        return new_state
