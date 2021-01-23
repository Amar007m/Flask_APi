from flask import Flask
from flask_sqlalchemy import  SQLAlchemy
from flask_cors import CORS
from api.Blog.blog_routes import blogs
import click
from flask.cli import with_appcontext
from werkzeug.security import generate_password_hash

db = SQLAlchemy()
app.register_blueprint(blogs)


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://flaskdatabase.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    CORS(app)

    db.init_app(app)
    return app





@click.command(name='create_admin')   
    @with_appcontext
    def create_admin():
        admin=User(email="admin_email_address",password="admin_password")
        admin.password = generate_password_hash(admin.password,'sha256',salt_length=12)
        db.session.add(admin)
        db.session.commit()
 
    app.cli.add_command(create_admin)



app.config['JWT_SECRET_KEY']='Kicevo1@'
jwt=JWTManager(app)