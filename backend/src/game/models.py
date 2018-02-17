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
        self.state = LockState.CLOSED


class LockState(Enum):
    OPEN = 'open'
    CLOSED = 'closed'


class Lock():
    def __init__(self, label=None, address=None, puzzles=[]):
        self.label = label
        self.address = address
        self.puzzles = puzzles
        self.state = LockState.CLOSED


class State():
    def __init__(self, locks=[]):
        self.locks = locks
