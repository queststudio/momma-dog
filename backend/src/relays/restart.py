def restart_creator(set_state, configuration):
    def restart():
        address = configuration.Plugins['relays'].Properties['ADDRESS']
        port = configuration.Plugins['relays'].Properties['PORT']
        
        set_state(address, port, False)
        set_state(address, port, True)

    return restart
