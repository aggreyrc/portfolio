from flask import request, make_response, session, Flask, jsonify
from flask_migrate import Migrate
from flask_restful import Resource,Api
from flask_cors import CORS
from dotenv import load_dotenv
load_dotenv()
import os

from models import Project, db

import cloudinary
import cloudinary.uploader

# Configure Cloudinary
cloudinary.config(
    cloud_name="your_cloud_name",
    api_key="your_api_key",
    api_secret="your_api_secret"
)


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI', 'sqlite:///app.db')
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

# Projects
class Projects(Resource):
    # fetching all projects
    def get(self):
        project_list = []
        projects = Project.query.all()
        for project in projects:
            project_dict = {
                "id": project.id,
                "name": project.name,
                "description": project.description,
                "github_url": project.github_url
            }
            project_list.append(project_dict)
        return make_response(project_list, 200)
    
api.add_resource(Projects, '/projects')


if __name__ == '__main__':
   port = int(os.environ.get("PORT", 5000))
   app.run(host="0.0.0.0", port=port)