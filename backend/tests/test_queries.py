import pytest
from unittest import TestCase

from src.game.queries import PuzzleExistsQuery, ReporterExistsQuery, PuzzlesQuery, PuzzleQuery, LocksQuery, \
    SwitchesQuery
from src.game.models import State, Puzzle, Lock, PuzzleState, Switch

# ToDo split this file

test_puzzle = Puzzle(6, 2)

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
        test_puzzle,
        Puzzle(6, 3)
    ])
], switches=[
    Switch(),
    Switch(),
    Switch(),
])


class TestPuzzleExistsQuery(TestCase):
    def test_perform__all_matches__returns_true(self):
        target = PuzzleExistsQuery(
            Puzzle(test_puzzle.reporter, test_puzzle.local_address))

        actual = target.perform(test_state)

        assert True == actual

    def test_perform__no_match__returns_false(self):
        targets = [PuzzleExistsQuery(Puzzle(4, 6)),
                   PuzzleExistsQuery(Puzzle(0, 0)),
                   PuzzleExistsQuery(Puzzle(7, 3))]

        actual_returns = [target.perform(
            test_state) == False for target in targets]

        assert all(actual_returns)


class TestPuzzleQuery(TestCase):
    def test_perform__all_matches__returns_puzzle(self):
        target = PuzzleQuery(
            Puzzle(test_puzzle.reporter, test_puzzle.local_address))

        actual = target.perform(test_state)

        assert test_puzzle == actual

    def test_perform__no_match__returns_none(self):
        targets = [PuzzleQuery(Puzzle(4, 6)),
                   PuzzleQuery(Puzzle(0, 0)),
                   PuzzleQuery(Puzzle(7, 3))]

        actual_returns = [target.perform(
            test_state) == None for target in targets]

        assert all(actual_returns)


class TestPuzzlesQuery(TestCase):
    def test_perform____returns_all_puzzles(self):
        target = PuzzlesQuery()

        actual = target.perform(test_state)

        assert len(actual) == 8


class TestReporterExistsQuery(TestCase):
    def test_perform__reporter_exists__returns_true(self):
        target = ReporterExistsQuery(test_puzzle.reporter)

        actual = target.perform(test_state)

        assert True == actual

    def test_perform__reporter_doesnt_exist__returns_false(self):
        targets = [ReporterExistsQuery(100)]

        actual_returns = [target.perform(
            test_state) == False for target in targets]

        assert all(actual_returns)


class TestLocksQuery(TestCase):
    def test_perform____returns_all_locks(self):
        target = LocksQuery()

        actual = target.perform(test_state)

        assert len(actual) == 6


class TestSwitchesQuery(TestCase):
    def test_perform____returns_all_switches(self):
        target = SwitchesQuery()

        actual = target.perform(test_state)

        assert len(actual) == 3
