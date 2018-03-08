from src.relays.factory import RelayFactory


# ToDo use logger

def _is_port_valid(port):
    return port > 7 or port < 0


class RelayService:
    def __init__(self, factory: RelayFactory):
        self._factory = factory

    def set_state(self, address, port, state):
        if not _is_port_valid(port):
            print("Invalid port!")
            return

        try:
            pcf = self._factory.create(address)
            print(pcf.port[port])
            print(state)
            if pcf.port[port] != state:
                print('happens')
                pcf.port[port] = state
        except IOError:
            print('I2C not available')
