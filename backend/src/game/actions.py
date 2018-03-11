from copy import deepcopy
from src.game.models import State, Puzzle, Switch, SwitchState, PuzzleState


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
                    if (puzzle.state != PuzzleState.SOLVED):
                        puzzle.state = self.puzzle.state

        return new_state


class UpdateSwitchAction(Action):
    def __init__(self, id: int, state: SwitchState):
        self.id = id
        self.state = state

    def act(self, state: State):
        new_state = deepcopy(state)
        for switch in new_state.switches:
            if (switch.id == self.id):
                switch.state = self.state

        return new_state


class RestartAction(Action):
    def act(self, state: State):
        new_state = deepcopy(state)
        new_state.game = state.game + 1
        return new_state
