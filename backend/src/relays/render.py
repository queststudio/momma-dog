from src.game.models import LockState, Lock, State, SwitchState, Switch
from src.relays.set_state import set_state

i2c_port_num = 1


# ToDo use logger

def render(address, port, state):
    set_state(address, port, state)


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
