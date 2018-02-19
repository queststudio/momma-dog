from enum import Enum


class PuzzleState(Enum):
    SOLVED = 'solved'
    NOT_SOLVED = 'not solved'
    UNKNOWN = 'unknown'
    NOT_PRESENT = 'not present'


class Puzzle():
    def __init__(self, reporter=None, local_address=None):
        self.reporter = reporter
        self.local_address = local_address
        self.state = PuzzleState.UNKNOWN

    def serialize(self):
        return {
            'reporter': self.reporter,
            'local_address': self.local_address,
            'state': self.state.value,
        }


class LockState(Enum):
    OPEN = 'open'
    CLOSED = 'closed'


class Lock():
    def __init__(self, label=None, address=None, port=None, puzzles=[]):
        self.label = label
        self.address = address
        self.port = port
        self.puzzles = puzzles

    @property
    def state(self):
        open = all([puzzle.state == PuzzleState.SOLVED for puzzle in self.puzzles])
        return LockState.OPEN if open else LockState.CLOSED

    def serialize(self):
        return {
            'label': self.label,
            'address': self.address,
            'port': self.port,
            'puzzles': [puzzle.serialize() for puzzle in self.puzzles],
            'state': self.state.value,
        }


class State():
    def __init__(self, locks=[]):
        self.locks = locks
