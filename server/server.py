from app import app, db
from app.models import User, Project, Task

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Project': Project, 'Task': Task}

#app.run(host='0.0.0.0')
