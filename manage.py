from app import create_app,db
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from app.models import User, Pitch, Comment



#Creating app instance
app = create_app('production')
manager = Manager(app)
manager.add_command('server',Server)
migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)
@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('test')
    unittest.TextTestRunner(verbosity=2).run(tests)
@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User, Pitch = Pitch, Comment = Comment)
if __name__ == '__main__':
    manager.run()

# app = create_app('development')

# manager = Manager(app)
# migrate = Migrate(app, db)

# manager.add_command('server', Server)
# manager.add_command('db', MigrateCommand)

# @manager.shell
# def add_shell_context():
#     return {'db': db, 'User': User, 'Pitch': Pitch, 'Comment': Comment}

# @manager.command
# def test():
#     import unittest
#     tests = unittest.TestLoader().discover('tests')
#     unittest.TextTestRunner(verbosity=2).run(tests)



# if __name__ == "__main__":
#     manager.run()