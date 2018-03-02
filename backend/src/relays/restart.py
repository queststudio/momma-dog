from src.relays.set_state import set_state


def restart(): # ToDo move that to some kind of settings
    set_state(52, 3, True)
    set_state(52, 3, False)
