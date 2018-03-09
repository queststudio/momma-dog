from src.game.models import LockState, Lock, State, SwitchState, Switch
from src.relays.service import RelayService
from src.relays.factory import RelayFactory, create_pcf

# ToDo use logger
factory = RelayFactory(1, create_pcf)
service = RelayService(factory)


def render(address, port, state):
    print('Rendering: ' + str(address) + ' ' + str(port) + ' ' + str(state))
    service.set_state(address, port, state)


def render_lock(lock: Lock):
    render(lock.address, lock.port, False if lock.state == LockState.OPEN else True)


def render_switch(switch: Switch):
    render(switch.address, switch.port, False if switch.state == SwitchState.ON else True)


def render_state(state: State):
    print('Rendering state on the relays.')
    print('Locks:')
    for lock in state.locks:
        render_lock(lock)
    print('Switches:')
    for switch in state.switches:
        render_switch(switch)
