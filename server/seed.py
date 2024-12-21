from models import Project,db
from datetime import datetime, timedelta,timezone
from app import app

def seed_data():
    with app.app_context():
        db.drop_all()
        db.create_all()
        
        # creating projects
        project1 = Project(
            name='Project Tracker',
            description='A project tracker for managing projects',
            github_url = 'https://github.com/aggreyrc/Project-Tracker-frontend',
        )
        
        # Adding projects to session
        db.session.add(project1)
        db.session.commit()
        
if __name__== "__main__":
    seed_data()
    