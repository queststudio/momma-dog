from os import environ
from src.config import config_local, config_museum

__configurations = {
    config_local.configuration.Environment: config_local.configuration,
    config_museum.configuration.Environment: config_museum.configuration
}

__environment = environ['ENVIRONMENT']
print(f'starting environment: {__environment}')

configuration = __configurations[__environment]
