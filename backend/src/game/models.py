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

    def __eq__(self, other):
        return self.reporter == other.reporter \
               and self.local_address == other.local_address \
               and self.state == other.state


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

    def __eq__(self, other):
        return self.label == other.label \
               and self.address == other.address \
               and self.port == other.port \
               and all([puzzle in other.puzzles for puzzle in self.puzzles]) \
               and len(self.puzzles) == len(other.puzzles)


class State():
    def __init__(self, locks=[]):
        self.locks = locks

    def __eq__(self, other):
        return all([lock in other.locks for lock in self.locks]) \
               and len(self.locks) == len(other.locks)