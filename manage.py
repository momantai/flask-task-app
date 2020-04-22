from app import create_app
from app import db, User, Task

from flask_script import Manager, Shell
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand

from config import config

config_class = config['development']
app = create_app(config_class)
migrate = Migrate(app, db)

def make_shell_context():
    return dict(app=app, db=db, User=User, Task=Task)

if __name__ == '__main__':
    manager = Manager(app)

    # Registramos un nueevo shell en el proyecto. Para trabajar con los modelos
    # a traves de clases y objetos.
    manager.add_command('shell', Shell(make_context=make_shell_context))

    # Migraciones
    # python3 manage.py db init (esto solo la primera vez sin aun no se tiene la carpeta migrations)
    # python3 manage.py db migration
    # python3 manage.py db upgrade
    manager.add_command('db', MigrateCommand)
    
    @manager.command
    def test():
        import unittest
        tests = unittest.TestLoader().discover('tests')
        unittest.TextTestRunner().run(tests)

    manager.run()