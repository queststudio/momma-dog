from src.api.endpoints.health import Health
from src.api.endpoints.locks import Locks
from src.api.endpoints.puzzles import Puzzles, ReporterPuzzles
from src.api.endpoints.reporters import Reporters
from src.api.endpoints.switches import Switches, Switch
from src.api.endpoints.games import CurrentGame

api_base = '/api'


def register_apis(register_resource, dependencies):

    def register_with_dependencies(resource, *urls, **kwargs):
        return register_resource(resource, *urls, **kwargs, resource_class_kwargs=dependencies)

    register_with_dependencies(Health, api_base + '/health')
    register_with_dependencies(Locks, api_base + '/locks')
    register_with_dependencies(Puzzles, api_base + '/puzzles')
    register_with_dependencies(
        ReporterPuzzles, api_base + '/reporters/<reporter>/puzzles/<int:local_address>')
    register_with_dependencies(Reporters, api_base + '/reporters/<reporter>')
    register_with_dependencies(Switch, api_base + '/switches/<int:id>')
    register_with_dependencies(Switches, api_base + '/switches')
    register_with_dependencies(CurrentGame, api_base + '/games/current')
