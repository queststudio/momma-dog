from src.game.models import State, Lock, Puzzle

init_state = State(locks=[
    Lock('first', 1, [
        Puzzle(reporter=1, local_address=1),
        Puzzle(reporter=1, local_address=2)
    ]),
    Lock('two', 2, [
        Puzzle(2, 5)
    ]),
    Lock('three', 3, [
        Puzzle(3, 6)
    ]),
    Lock('four', 4, [
        Puzzle(4, 7)
    ]),
    Lock('five', 5, [
        Puzzle(4, 8)
    ])
])


class Game():

    def __init__(self, state=init_state):
        self.state = state

    def get_locks(self):
        return self.state.locks

    def get_puzzles(self):
        return [puzzle for lock in self.state.locks for puzzle in lock.puzzles]
