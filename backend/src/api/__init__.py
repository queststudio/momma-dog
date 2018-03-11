from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from src.api.register_apis import register_apis
from src.api.create_store import create_store

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})
api = Api(app)

store = create_store()
store.trigger()


register_apis(api.add_resource)

if __name__ == '__main__':
    app.run(debug=True)