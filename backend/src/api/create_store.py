from src.relays.set_state import set_state
from src.relays.render import render_state
from src.game.store import Store, init_state

from src.game.middlewares import restart_middleware_creator
from src.relays.restart import restart_creator

restart = restart_creator(set_state)
restart_middleware = restart_middleware_creator(restart)


def create_store():
    store = Store(init_state, [restart_middleware])
    store.subscribe(render_state)
    return store
