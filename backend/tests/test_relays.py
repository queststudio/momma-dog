from unittest import TestCase
from unittest.mock import patch, MagicMock, Mock
from src.relays.service import RelayService
from src.relays.factory import RelayFactory

magic_mock = MagicMock()


class TestRelayFactory(TestCase):
    def test_create__empty__creates_new_relay(self):
        def create_relay(port, address): return {'address': address}
        target = RelayFactory(1, create_relay)

        actual = target.create(11)

        assert actual.get('address') == 11

    def test_create__called_twice__returns_the_same_object(self):
        def create_relay(port, address): return {'address': address}
        target = RelayFactory(1, create_relay)

        actual1 = target.create(11)
        actual2 = target.create(11)

        assert actual1 is actual2


def get_relay_mock(return_value):
    relay_mock = magic_mock()
    relay_mock.port = magic_mock()
    relay_mock.port.__getitem__ = Mock(return_value=return_value)
    relay_mock.port.__setitem__ = Mock(return_value=None)
    return relay_mock


def get_factory_mock(relay_mock):
    factory_mock = magic_mock()
    factory_mock.create = Mock(return_value=relay_mock)
    return relay_mock


class TestRelayService(TestCase):
    def test_set_state__state_is_different__state_changed(self):
        relay_mock = get_relay_mock(return_value=True)
        factory_mock = get_factory_mock(relay_mock)
        target = RelayService(factory_mock)

        target.set_state(11, 20, False)

        relay_mock.__setitem__.assert_called_once_with(20, False)

    def test_set_state__state_is_the_same__nothing_happens(self):
        relay_mock = get_relay_mock(return_value=True)
        factory_mock = get_factory_mock(relay_mock)
        target = RelayService(factory_mock)

        target.set_state(11, 20, True)

        relay_mock.__setitem__.assert_not_called()
