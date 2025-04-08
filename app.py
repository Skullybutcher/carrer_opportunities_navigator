from flask import Flask
from flask_cors import CORS
from api.routes import api
from database.db import Base, engine

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    # Enable CORS
    CORS(app)
    
    # Register blueprints
    app.register_blueprint(api, url_prefix='/api')
    
    # Create database tables
    Base.metadata.create_all(bind=engine)
    
    @app.route('/')
    def index():
        return "Career Opportunities Navigator API"
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
