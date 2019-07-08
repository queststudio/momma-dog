from src.config.model import Configuration, Plugin

relays_plugin = Plugin(Name='relays', Properties={
    'ENABLED': True,
    'ADDRESS': 58,
    'PORT': 4
})

configuration = Configuration(Environment='MUSEUM',
                              Plugins={'relays': relays_plugin})
