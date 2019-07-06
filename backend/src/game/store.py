from functools import reduce

from src.game.models import State, Lock, Puzzle, Switch
from src.game.actions import Action
from src.game.queries import Query

def _combine_middlewares(middlewares):
    empty_middleware = lambda next: lambda action: next(action)
    combine_middlewares = lambda first, second: lambda next: first(second(next))
    middleware = reduce(combine_middlewares, [empty_middleware] + middlewares)
    return middleware

class Store():
    def __init__(self, initial_state=None, middlewares=[]):
        self.state = initial_state
        self._subscriber = None

        self._middleware = _combine_middlewares(middlewares)

    def act(self, action: Action):
        act = lambda action: action.act(self.state)
        new_state = self._middleware(act)(action)

        if new_state == self.state:
            return

        self.state = new_state

        self.trigger()

    def trigger(self):
        if self._subscriber:
            self._subscriber(self.state)

    def perform_query(self, query: Query):
        return query.perform(self.state)

    def subscribe(self, subscriber):
        self._subscriber = subscriber


init_state = State(locks=[
    Lock('Гнев', 56, 0, [
        Puzzle('62:01:94:70:63:9d', 8) 
    ]),
    Lock('Уныние', 56, 1, [
        Puzzle('a2:20:a6:02:08:b4', 11) 
    ]),
    Lock('Гордыня - свет', 56, 2, [
        Puzzle('5e:cf:7f:89:2a:9a', 12) 
    ]),
    Lock('Гордыня - код', 56, 3, [
        Puzzle('5e:cf:7f:89:2a:9a', 13) 
    ]),
    Lock('Алчность', 56, 4, [
        Puzzle('a2:20:a6:13:2d:80', 14) 
    ]),
    Lock('Обжорство - конфеты', 56, 7, [
        Puzzle('62:01:94:70:67:b3', 21) 
    ]),
    Lock('Обжорство - фрукты', 57, 0, [
        Puzzle('62:01:94:70:67:b3', 22),
        Puzzle('62:01:94:70:67:b3', 23) 
         ]),
  
    Lock('Сцена КОД', 57, 7, [
        Puzzle('a2:20:a6:02:67:a9', 25)
    ]),

    Lock('Театр ВЫХОД ', 57, 6, [
        Puzzle('a2:20:a6:12:2a:9b', 24)
    ]),
   
              
    
    Lock('темная комната ВЫХОД', 57, 5, [
        Puzzle('5e:cf:7f:1a:b6:2e', 9)
    ]),
 
    Lock('Крест', 61, 5, [
        Puzzle('5e:cf:7f:87:56:5c', 20)
    ]),
    Lock('сундук 1', 58, 2, [
        Puzzle('5e:cf:7f:87:56:52', 15)
    ]),
    Lock('сундук 2', 58, 5, [
        Puzzle('5e:cf:7f:1a:ba:df', 16)
    ]),
    Lock('сундук 3', 58, 1, [
        Puzzle('5e:cf:7f:1b:60:98', 17)
    ]),
    Lock('сундук 4', 58, 0, [
        Puzzle('62:01:94:70:58:ed', 18)
    ])

], switches=[

    Switch(9, 'Гардероб дверь  ', 61, 3),
    Switch(1, 'Зависть', 56, 5),
    Switch(2, 'Похоть', 56, 6),
    Switch(3, 'Выход 7грехов', 57, 2),
  
    Switch(4, 'Зеркало (нажать чтобы задача заработала)', 58, 7),
    Switch(5, 'Сцена Театр ниша ', 57, 1),
   
    Switch(7, 'Темная комната - LED(Включатель!)', 58, 3),
    Switch(6, 'Свет темная комната - LED(Выключатель)', 57, 3),
    
    Switch(10, 'крест подсветка ', 58, 6),
    Switch(11, ' Финал ', 61, 0),
    
    Switch(13, ' дверь 1 -Красная комната', 61, 7),
    Switch(14, ' дверь 2 -Театр  ', 61, 1),
    Switch(15, ' дверь 3 -Кладбище', 61, 6),
    Switch(16, ' дверь 4 -Тёмная', 61, 2),
    
    Switch(12, 'Рестарт(перед перезагрузкой)', 58, 4),

], game=1)

store = Store(init_state)
