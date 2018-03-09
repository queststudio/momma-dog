# ToDo use logger

def create_pcf(port, address):
    try:
        from pcf8574 import PCF8574
        return PCF8574(port, address)
    except ImportError:
        print('Couldn\'t find module pcf8574')


class RelayFactory:
    def __init__(self, i2c_port, create_relay):
        self._pcfs = {}
        self.i2c_port = i2c_port
        self._create_relay = create_relay

    def create(self, address):
        if not self._pcfs.get(address):
            self._pcfs[address] = self._create_relay(self.i2c_port, address)

        return self._pcfs.get(address)

