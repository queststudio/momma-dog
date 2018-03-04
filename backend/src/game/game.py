from src.game.models import State, Lock, Puzzle, Switch
from src.game.actions import Action
from src.game.queries import Query


class Game():

    def __init__(self, state=None):
        self.state = state

    def get_locks(self):  # ToDo move to queries
        return self.state.locks

    def get_puzzles(self):  # ToDo move to queries
        return [puzzle for lock in self.state.locks for puzzle in lock.puzzles]

    def act(self, action: Action):
        new_state = action.act(self.state)

        if new_state == self.state:
            return

        self.state = new_state

        self.trigger()

    def trigger(self):
        if self.__subscriber:
            self.__subscriber(self.state)

    def perform_query(self, query: Query):
        return query.perform(self.state)

    def subscribe(self, subscriber):
        self.__subscriber = subscriber


init_state = State(locks=[
    Lock('Гнев', 56, 0, [
        Puzzle('62:01:94:70:63:9d', 8)  # выставлен
    ]),
    Lock('Уныние', 56, 1, [
        Puzzle('a2:20:a6:02:08:b4', 11)  # выставлен
    ]),
    Lock('Гордыня - свет', 56, 2, [
        Puzzle('62:01:94:70:62:2e', 12)  # вставить мак гордыня
    ]),
    Lock('Гордыня - код', 56, 3, [
        Puzzle('62:01:94:70:62:2e', 13)  # вставить мак гордыня
    ]),
    Lock('Алчность', 56, 4, [
        Puzzle('a2:20:a6:13:2d:80', 14)  # вставлен
    ]),
    Lock('Обжорство - конфеты', 56, 7, [
        Puzzle('62:01:94:70:67:b3', 21)  # вставлен
    ]),
    Lock('Обжорство - фрукты', 57, 0, [
        Puzzle('62:01:94:70:67:b3', 22),
        Puzzle('62:01:94:70:67:b3', 23)  # вставилен
    ]),
    Lock('Сцена КОД', 57, 7, [
        Puzzle('a2:20:a6:02:67:a9', 25)  # вставлен
    ]),
    Lock('Зеркало ', 58, 7, [
        Puzzle('5e:cf:7f:1b:7a:e8', 19)  # вставлено
    ]),
    Lock('Театр ВЫХОД ', 57, 6, [
        Puzzle('a2:20:a6:12:2a:9b', 24)  # вставлено
    ]),
    Lock('темная комната - LED', 57, 4, [
        Puzzle('62:01:94:70:60:70', 9)  # вставить MAC
    ]),
    Lock('темная комната ВЫХОД', 57, 5, [
        Puzzle('5e:cf:7f:1a:b6:2e', 10)  # вставлен
    ]),
    Lock('Крест', 58, 6, [
        Puzzle('5e:cf:7f:87:56:5c', 20)  # вставлен
    ]),
    Lock('сундук 1', 58, 1, [
        Puzzle('62:01:94:70:58:ed', 15)  # вставить MAC
    ]),
    Lock('сундук 2', 58, 2, [
        Puzzle('62:01:94:70:58:ed', 16)  # вставить MAC
    ]),
    Lock('сундук 3', 58, 0, [
        Puzzle('62:01:94:70:58:ed', 17)  # вставить MAC
    ]),
    Lock('сундук 4', 58, 5, [
        Puzzle('62:01:94:70:58:ed', 18)  # вставить MAC
    ])

], switches=[
    Switch(1, 'Зависть', 56, 5),  # добавлен
    Switch(2, 'Похоть', 56, 6),  # добавлен
    Switch(3, 'Выход 7грехов', 57, 2),  # добавлен
    Switch(4, 'Свет красная комната', 5, 6),  # добавить i2c
    Switch(5, 'Сцена Театр ниша ', 57, 1),  # добавлен
    Switch(6, 'Свет Театр весь', 69, 6),  # добавить i2c
    Switch(7, 'Свет Театр бра', 69, 5),  # добавить i2c
    Switch(8, 'Свет Коридор  ', 69, 4),  # добавить i2c
    Switch(9, 'Свет Тёмная комната  ', 69, 3),  # добавить i2c
    Switch(10, 'Свет Кладбище  ', 61, 2),  # добавить i2c
    Switch(11, ' Финал ', 61, 0),  # добавить i2c
    Switch(12, 'Рестарт', 58, 4),  # добавлен
    Switch(13, ' дверь 1 -Красная комната', 61, 7),  # добавить i2c
    Switch(14, ' дверь 2 -Театр  ', 61, 1),  # добавить i2c
    Switch(15, ' дверь 3 -Кладбище', 61, 6),  # добавить i2c
    Switch(16, ' дверь 4 -Тёмная', 61, 2),  # добавить i2c
    
])
# ToDo
# Puzzle chest_2_puzzles [1] = {
#   Puzzle(16)
# };
# Lock chest_2_lock(chest_2_puzzles, 1, 16);
# 
# Puzzle chest_3_puzzles [1] = {
#   Puzzle(17)
# };
# Lock chest_3_lock(chest_3_puzzles, 1, 17);
# 
# Puzzle chest_4_puzzles [1] = {
#   Puzzle(18)
# };
# Lock chest_4_lock(chest_4_puzzles, 1, 18);
# 
# Puzzle mirror_puzzles [1] = {
#   Puzzle(19)
# };
# Lock mirror_lock(mirror_puzzles, 1, 19);
# 
# Puzzle crucifix_puzzles [1] = {
#   Puzzle(20)
# };
# Lock crucifix_lock(crucifix_puzzles, 1, 20);
# 
# Puzzle gula_candy_puzzles [1] = {
#   Puzzle(21)
# };
# Lock gula_candy_lock(gula_candy_puzzles, 1, 21);
# 
# Puzzle gula_fruit_puzzles [2] = {
#   Puzzle(22),
#   Puzzle(23)
# };
# Lock gula_fruit_lock(gula_fruit_puzzles, 2, 22);
# 
#   Puzzle code_panel1_puzzles [1] = {
#   Puzzle(24),
# };
# Lock code_panel1_lock(code_panel1_puzzles, 1, 23);
# 
#   Puzzle code_panel2_puzzles [1] = {
#   Puzzle(25),  
# };
# Lock code_panel2_lock(code_panel2_puzzles, 1, 24);
# 
#     Puzzle EXIT_puzzles [1] = {
#     Puzzle(26),
# };
# Lock EXIT_lock(EXIT_puzzles, 1, 25);

game = Game(init_state)
