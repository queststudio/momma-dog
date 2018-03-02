i2c_port_num = 1


# ToDo use logger
class PCF:
    def __init__(self):
        self.pcfs = {}

    def set_state(self, address, port, state):
        try:
            if not self.pcfs.get(address):
                from pcf8574 import PCF8574
                self.pcfs[address] = PCF8574(i2c_port_num, address)
            self.pcfs.get(address).port[port] = state
        except ImportError:
            print('Couldn\'t find module pcf8574')
        except IOError:
            print('I2C not available')


singleton = PCF()


def set_state(address, port, state):
    print('Rendering: ' + str(address) + ' ' + str(port) + ' ' + str(state))
    singleton.set_state(address, port, state)
