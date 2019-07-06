from src.game.actions import Action, RestartAction


def restart_middleware_creator(restart):
    def restart_middleware(next):
        def apply(action: Action):
            if isinstance(action, RestartAction):
                restart()

            return next(action)
        return apply
    return restart_middleware
