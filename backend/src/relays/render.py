from src.game.models import LockState, Lock, State, SwitchState, Switch

i2c_port_num = 1

#ToDo use logger


def render(address, port, state):
    try:
        from pcf8574 import PCF8574
        pcf = PCF8574(i2c_port_num, address)
        pcf.port[port] = state
    except ImportError:
        print('Couldn\'t find module pcf8574')
    except IOError:
        print('I2C not available')


def render_lock(lock: Lock):
    print('Rendering: ' + str(lock.address) + ' ' + str(lock.port) + ' ' + lock.state.value)
    render(lock.address, lock.port, False if lock.state == LockState.OPEN else True)


def render_switch(switch: Switch):
    print('Rendering: ' + str(switch.address) + ' ' + str(switch.port) + ' ' + switch.state.value)
    render(switch.address, switch.port, False if switch.state == SwitchState.ON else True)


def render_state(state: State):
    print('Rendering state on the relays.')
    print('Locks:')
    for lock in state.locks:
        render_lock(lock)
    print('Switches:')
    for switch in state.switches:
        render_switch(switch)
