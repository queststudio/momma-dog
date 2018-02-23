from flask import Flask, jsonify
from flask_restful import Api
from flask_cors import CORS

from src.register_apis import register_apis
from src.relays.render import render_state
from src.game.game import game

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})
api = Api(app)

@app.route('/')
def index():
    return "Remote control is under construction."

game.subscribe(render_state)
register_apis(api.add_resource)

if __name__ == '__main__':
    app.run(debug=True)