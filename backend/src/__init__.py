from flask import Flask, jsonify
from flask_restful import Api

from src.endpoints.register_apis import register_apis

app = Flask(__name__)
api = Api(app)

@app.route('/')
def index():
    return "Hello, World!"

register_apis(api.add_resource)

if __name__ == '__main__':
    app.run(debug=True)