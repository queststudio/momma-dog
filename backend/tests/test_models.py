import pytest
from unittest import TestCase

from src.game.models import State, Puzzle, Lock, PuzzleState, LockOperator, LockState


class TestLock(TestCase):
    def test_open__operator_or_none_is_solved__state_is_closed(self):
        puzzle1 = Puzzle(6, 1)
        puzzle2 = Puzzle(6, 2)
        puzzle3 = Puzzle(6, 3)
        target = Lock('six', 0x3F, 6, [puzzle1, puzzle2, puzzle3], LockOperator.OR)

        assert target.state is LockState.CLOSED

    def test_open__operator_or_one_is_solved__state_is_open(self):
        puzzle1 = Puzzle(6, 1)
        puzzle2 = Puzzle(6, 2)
        puzzle2.state = PuzzleState.SOLVED
        puzzle3 = Puzzle(6, 3)
        target = Lock('six', 0x3F, 6, [puzzle1, puzzle2, puzzle3], LockOperator.OR)

        assert target.state is LockState.OPEN

    def test_open__operator_and_none_is_solved__state_is_closed(self):
        puzzle1 = Puzzle(6, 1)
        puzzle2 = Puzzle(6, 2)
        puzzle3 = Puzzle(6, 3)
        target = Lock('six', 0x3F, 6, [puzzle1, puzzle2, puzzle3], LockOperator.AND)

        assert target.state is LockState.CLOSED

    def test_open__operator_or_one_is_not_solved__state_is_closed(self):
        puzzle1 = Puzzle(6, 1)
        puzzle2 = Puzzle(6, 2)
        puzzle2.state = PuzzleState.SOLVED
        puzzle3 = Puzzle(6, 3)
        puzzle3.state = PuzzleState.SOLVED
        target = Lock('six', 0x3F, 6, [puzzle1, puzzle2, puzzle3], LockOperator.AND)

        assert target.state is LockState.CLOSED

    def test_open__operator_or_all_are_solved__state_is_open(self):
        puzzle1 = Puzzle(6, 1)
        puzzle1.state = PuzzleState.SOLVED
        puzzle2 = Puzzle(6, 2)
        puzzle2.state = PuzzleState.SOLVED
        puzzle3 = Puzzle(6, 3)
        puzzle3.state = PuzzleState.SOLVED
        target = Lock('six', 0x3F, 6, [puzzle1, puzzle2, puzzle3], LockOperator.AND)

        assert target.state is LockState.OPEN
