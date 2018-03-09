from src.api.endpoints.health import Health
from src.api.endpoints.locks import Locks
from src.api.endpoints.puzzles import Puzzles, ReporterPuzzles
from src.api.endpoints.reporters import Reporters
from src.api.endpoints.switches import Switches, Switch

api_base = '/api'

def register_apis(register_resource):
    register_resource(Health, api_base + '/health')
    register_resource(Locks, api_base + '/locks')
    register_resource(Puzzles, api_base + '/puzzles')
    register_resource(ReporterPuzzles, api_base + '/reporters/<reporter>/puzzles/<int:local_address>')
    register_resource(Reporters, api_base + '/reporters/<reporter>')
    register_resource(Switch, api_base + '/switches/<int:id>')
    register_resource(Switches, api_base + '/switches.api.')