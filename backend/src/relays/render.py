from src.game.models import LockState, Lock, State

i2c_port_num = 1


def render_lock(lock: Lock):
    print('Rendering: ' + lock.address + ' ' + lock.port + ' ' + lock.state.value)
    try:
        from pcf8574 import PCF8574
        pcf = PCF8574(i2c_port_num, lock.address)
        pcf.port[lock.port] = False if lock.state == LockState.OPEN else True
    except ModuleNotFoundError:
        print('Couldn\'t find module pcf8574')


def render_state(state: State):
    print('Rendering state on the relays.')
    for lock in state.locks:
        render_lock(lock)
