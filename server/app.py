from flask import request, make_response, session, Flask, jsonify
from flask_migrate import Migrate
from flask_restful import Resource,Api
from flask_cors import CORS
from dotenv import load_dotenv
load_dotenv()
import os

from models import Project, db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)
migrate = Migrate(app, db)
db.init_app(app)
api = Api(app)

# Home
class Home(Resource):
    def get(self):
        return {
               "message": " 🗂️ Welcome to tmy portfolio API 🗂️",
               "api-version": "vi",
               "description": "Portfolio",
               "available_endpoints": [
                   "/projects"
               ]
          },200
api.add_resource(Home, '/')