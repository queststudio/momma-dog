from src.endpoints.health import Health
from src.endpoints.locks import Locks
from src.endpoints.puzzles import Puzzles

api_base = '/api'

def register_apis(register_resource):
    register_resource(Health, f'{api_base}/health')
    register_resource(Locks, f'{api_base}/locks')
    register_resource(Puzzles, f'{api_base}/puzzles')