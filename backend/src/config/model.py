from collections import namedtuple
from typing import Dict

Plugin = ('Plugin', [('Name', str), ('Properties', dict)])
Plugins = Dict[str, Plugin]
Configuration = ('Configuration', [('Environment', str), ('Plugins', Plugins)])
