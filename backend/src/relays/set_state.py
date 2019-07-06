from src.game.models import LockState, Lock, State, SwitchState, Switch
from src.relays.service import RelayService
from src.relays.factory import RelayFactory, create_pcf

# ToDo use logger
factory = RelayFactory(1, create_pcf)
service = RelayService(factory)


def set_state(address, port, state):
    print('Setting state: ' + str(address) +
          ' ' + str(port) + ' ' + str(state))
    service.set_state(address, port, state)
