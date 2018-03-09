from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from src.api.register_apis import register_apis
from src.relays.render import render_state
from src.game.store import store

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})
api = Api(app)

store.subscribe(render_state)
store.trigger()

register_apis(api.add_resource)

if __name__ == '__main__':
    app.run(debug=True)