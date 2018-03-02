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
                if (puzzle.reporter == self.puzzle.reporter
                    and puzzle.local_address == self.puzzle.local_address):
                    return True

        return False


class PuzzleQuery(Query):
    def __init__(self, puzzle: Puzzle):
        self.puzzle = puzzle

    def perform(self, state: State):
        for lock in state.locks:
            for puzzle in lock.puzzles:
                if (puzzle.reporter == self.puzzle.reporter
                    and puzzle.local_address == self.puzzle.local_address):
                    return puzzle

        return None


class ReporterExistsQuery(Query):
    def __init__(self, reporter: str):
        self.reporter = reporter

    def perform(self, state: State):
        for lock in state.locks:
            for puzzle in lock.puzzles:
                if (puzzle.reporter == self.reporter):
                    return True

        return False


class SwitchesQuery(Query):
    def perform(self, state: State):
        return state.switches


class SwitchExistsQuery(Query):
    def __init__(self, id):
        self.id = id

    def perform(self, state: State):
        for switch in state.switches:
            if (str(switch.id) == str(self.id)):
                return True

        return False


class GameQuery(Query):
    def perform(self, state: State):
        return state.game
