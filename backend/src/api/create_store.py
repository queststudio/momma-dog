from src.relays.set_state import set_state
from src.relays.render import render_state
from src.game.store import Store, init_state
from src.game.middlewares import restart_middleware_creator
from src.relays.restart import restart_creator
from src.config import configuration


relays_enabled = 'relays' in configuration.Plugins
restart = restart_creator(set_state, configuration)
restart_middleware = restart_middleware_creator(restart)


def create_store():
    middlewares = []

    if relays_enabled:
        middlewares.append(restart_middleware)

    store = Store(init_state, middlewares)

    if relays_enabled:
        store.subscribe(render_state)

    return store
