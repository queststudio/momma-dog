i2c_port_num = 1


# ToDo use logger
class PCF:
    def __init__(self):
        self.pcfs = {}

    def set_state(self, address, port, state):
        if not self.pcfs.get(address):
            try:
                from pcf8574 import PCF8574
                pcf = PCF8574(i2c_port_num, address)
                pcf.port[port] = state
                self.pcfs[address] = PCF8574(i2c_port_num, address)
            except ImportError:
                print('Couldn\'t find module pcf8574')
            except IOError:
                print('I2C not available')


singleton = PCF()


def set_state(address, port, state):
    print('Rendering: ' + str(address) + ' ' + str(port) + ' ' + str(state))
    singleton.set_state(address, port, state)
