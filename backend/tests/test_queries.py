import pytest
from unittest import TestCase

from src.game.queries import PuzzleExistsQuery
from src.game.models import State, Puzzle, Lock, PuzzleState

test_state = State(locks=[
    Lock('first', 0x3F, 1, [
        Puzzle(1, 1),
        Puzzle(1, 2)
    ]),
    Lock('two', 0x3F, 2, [
        Puzzle(2, 5)
    ]),
    Lock('three', 0x3F, 3, [
        Puzzle(3, 6)
    ]),
    Lock('four', 0x3F, 4, [
        Puzzle(4, 7)
    ]),
    Lock('five', 0x3F, 5, [
    ]),
    Lock('six', 0x3F, 6, [
        Puzzle(6, 1),
        Puzzle(6, 2),
        Puzzle(6, 3)
    ])
])


class TestUpdatePuzzleAction(TestCase):
    def test_act__all_matches__returns_true(self):
        target = PuzzleExistsQuery(Puzzle(6, 2))

        actual = target.perform(test_state)

        assert True == actual

    def test_act__no_match__returns_false(self):
        targets = [PuzzleExistsQuery(Puzzle(4,6)),
                PuzzleExistsQuery(Puzzle(0,0)),
                PuzzleExistsQuery(Puzzle(7,3))]

        actual_returns = [target.perform for target in targets]

        assert all(actual_returns)