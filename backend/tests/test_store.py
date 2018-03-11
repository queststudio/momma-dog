import pytest
from unittest import TestCase
from unittest.mock import Mock, call

from src.game.store import Store
from src.game.actions import Action
from src.game.queries import Query
from src.game.models import State, Puzzle, Lock

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


class TestStore(TestCase):

    def test_act__updates_state(self):
        expected = {'some': 'object'}
        target = Store(test_state)
        test_action = Action()
        test_action.act = Mock(return_value=expected)

        target.act(test_action)

        assert expected == target.state

    def test_act__action_gets_state(self):
        target = Store(test_state)

        test_action = Action()

        def assertion(state):
            assert test_state == state
            return state

        test_action.act = assertion

        target.act(test_action)

    def test_act__state_changed__subscriber_triggered(self):
        expected = {'some': 'object'}
        target = Store(test_state)
        subscriber = Mock()
        target.subscribe(subscriber)
        test_action = Action()
        test_action.act = Mock(return_value=expected)

        target.act(test_action)

        subscriber.assert_called_once()

    def test_act__state_not_changed__subscriber_not_triggered(self):
        target = Store(test_state)
        subscriber = Mock()
        target.subscribe(subscriber)
        test_action = Action()
        test_action.act = lambda state: state

        target.act(test_action)

        subscriber.assert_not_called()

    def test_act__one_middleware__middleware_is_called(self):
        sideeffect = Mock()

        def middleware(next):
            def apply(action):
                sideeffect()
                next(action)

            return apply

        target = Store(test_state, [middleware])
        test_action = Action()

        target.act(test_action)

        sideeffect.assert_called_once()

    def test_act__two_middlewares__middlewares_are_called(self):
        sideeffect = Mock()

        def middleware1(next):
            def apply(action):
                sideeffect(1)
                next(action)

            return apply

        def middleware2(next):
            def apply(action):
                sideeffect(2)
                next(action)

            return apply

        target = Store(test_state, [middleware1, middleware2])
        test_action = Action()

        target.act(test_action)

        sideeffect.assert_has_calls([
            call(1),
            call(2)
        ])

    def test_perform__query_gets_state(self):
        target = Store(test_state)

        test_query = Query()

        def assertion(state): assert test_state == state

        test_query.perform = assertion

        target.perform_query(test_query)
