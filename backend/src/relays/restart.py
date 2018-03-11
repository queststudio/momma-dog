def restart_creator(set_state):
    def restart():
        # ToDo move that to some kind of settings
        address = 58
        port = 4

        set_state(address, port, False)
        set_state(address, port, True)

    return restart
