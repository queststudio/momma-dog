from src.game.models import State, Lock, Puzzle
from src.game.actions import Action
from src.game.queries import Query

class Game():

    def __init__(self, state=None):
        self.state = state

    def get_locks(self): #ToDo move to queries
        return self.state.locks

    def get_puzzles(self): #ToDo move to queries
        return [puzzle for lock in self.state.locks for puzzle in lock.puzzles]

    def act(self, action: Action):
        self.state = action.act(self.state)
        if self.__subscriber:
            self.__subscriber(self.state)
        
    def perform_query(self, query: Query):
        return query.perform(self.state)
    
    def subscribe(self, subscriber):
        self.__subscriber = subscriber



init_state = State(locks=[
    Lock('ira', 56, 0, [
        Puzzle(1, 8)
    ]),
    Lock('темная комната', 56, 1, [
        Puzzle(1, 9)
    ]),
    Lock('темная комната - свет', 56, 2, [
        Puzzle(1, 10)
    ]),
    Lock('acedia', 56, 3, [
        Puzzle(2, 11)
    ]),
    Lock('superbia - свет', 56, 4, [
        Puzzle(2, 12)
    ]),
    Lock('superbia - код', 56, 5, [
        Puzzle(2, 13)
    ]),
    Lock('avarice', 56, 6, [
        Puzzle(3, 14)
    ]),
    Lock('сундук - 1', 56, 7, [
        Puzzle(3, 15)
    ])
])
#ToDo
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
