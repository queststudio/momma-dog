import pytest
from unittest import TestCase

from src.game.actions import Action, UpdatePuzzleAction, RestartAction
from src.game.models import State, Puzzle, Lock, PuzzleState
from copy import deepcopy

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
],
    game=0)


class TestBasicAction(TestCase):
    def test_act__returns_another_object(self):
        target = Action()

        actual = target.act(test_state)

        assert not test_state is actual

    def test_act__returns_a_copy(self):
        target = Action()

        actual = target.act(test_state)

        assert test_state == actual


class TestUpdatePuzzleAction(TestCase):
    def test_act__returns_another_object(self):
        target = UpdatePuzzleAction(Puzzle(6, 2))

        actual = target.act(test_state)

        assert not test_state is actual

    def test_act__updates_specified_puzzle(self):
        puzzle = Puzzle(6, 2)
        puzzle.state = PuzzleState.NOT_PRESENT
        target = UpdatePuzzleAction(puzzle)

        actual = target.act(test_state)

        assert puzzle.state == actual.locks[5].puzzles[1].state

    def test_act__cant_drop_solved_puzzle(self):
        puzzle = Puzzle(6, 2)
        puzzle.state = PuzzleState.NOT_PRESENT
        target = UpdatePuzzleAction(puzzle)

        new_test_state = deepcopy(test_state)
        new_test_state.locks[5].puzzles[1].state = PuzzleState.SOLVED
        actual = target.act(new_test_state)

        assert PuzzleState.SOLVED == actual.locks[5].puzzles[1].state


class TestRestartAction(TestCase):
    def test_act__returns_another_object(self):
        target = RestartAction()

        actual = target.act(test_state)

        assert not test_state is actual

    def test_act__increments_game(self):
        target = RestartAction()

        actual = target.act(State(game=1))

        assert 2 == actual.game
