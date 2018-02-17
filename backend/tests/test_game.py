import pytest
from unittest import TestCase

from src.game.game import Game
from src.game.actions import Action
from src.game.queries import Query
from src.game.models import State, Puzzle, Lock

test_state = State(locks=[
    Lock('first', 1, [
        Puzzle(1, 1),
        Puzzle(1, 2)
    ]),
    Lock('two', 2, [
        Puzzle(2, 5)
    ]),
    Lock('three', 3, [
        Puzzle(3, 6)
    ]),
    Lock('four', 4, [
        Puzzle(4, 7)
    ]),
    Lock('five', 5, [
    ]),
    Lock('six', 6, [
        Puzzle(6, 1),
        Puzzle(6, 2),
        Puzzle(6, 3)
    ])
])


class TestGame(TestCase):

    def test_get_locks__returns_proper_items(self):
        target = Game(test_state)

        actual = target.get_locks()

        assert len(actual) == 6

    def test_get_puzzles__returns_proper_items_amount(self):
        target = Game(test_state)

        actual = target.get_puzzles()

        assert len(actual) == 8

    def test_act__updates_state(self):
        expected = {'some': 'object'}
        target = Game(test_state)
        test_action = Action()
        test_action.act = lambda state: expected

        target.act(test_action)

        assert expected == target.state

    def test_act__action_gets_state(self):
        target = Game(test_state)

        test_action = Action()
        def assertion(state): assert test_state == state
        test_action.act = assertion

        target.act(test_action)

    def test_act__updates_state(self):
        target = Game(test_state)

        test_query = Query()
        def assertion(state): assert test_state == state
        test_query.perform = assertion

        target.perform_query(test_query)

