from unittest import TestCase
from unittest.mock import Mock
from src.game.middlewares import restart_middleware_creator
from src.game.actions import Action, RestartAction


class TestRestartMiddleware(TestCase):
    def test_middleware__next_is_called(self):
        next = Mock()
        action = Action()
        middleware = restart_middleware_creator(None)

        middleware(next)(action)

        next.assert_called_once_with(action)

    def test_middleware__basic_action__restart_is_not_called(self):
        next = Mock()
        action = Action()
        restart = Mock()
        middleware = restart_middleware_creator(restart)

        middleware(next)(action)

        restart.assert_not_called()

    def test_middleware__restart_action__restart_called(self):
        next = Mock()
        action = RestartAction()
        restart = Mock()
        middleware = restart_middleware_creator(restart)

        middleware(next)(action)

        restart.assert_called_once()

    def test_middleware__basic_action__returns_what_next_returns(self):
        expected = {'some': 'thing'}
        next = Mock(return_value=expected)
        action = Action()
        middleware = restart_middleware_creator(None)

        actual = middleware(next)(action)

        assert expected == actual

    def test_middleware__restart_action__returns_what_next_returns(self):
        expected = {'some': 'thing'}
        next = Mock(return_value=expected)
        action = RestartAction()
        restart = Mock()
        middleware = restart_middleware_creator(restart)

        actual = middleware(next)(action)

        assert expected == actual
