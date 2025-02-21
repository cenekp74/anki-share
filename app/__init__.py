from flask import Flask
from celery import Celery, Task

app = Flask(__name__)
app.secret_key = 'dev'

app.config["CELERY"] = dict(
        broker_url="amqp://test:test@localhost:5672",
        task_ignore_result=True,
    )
app.config.from_pyfile('../instance/config.py')


def celery_init_app(app: Flask) -> Celery:
    class FlaskTask(Task):
        def __call__(self, *args: object, **kwargs: object) -> object:
            with app.app_context():
                return self.run(*args, **kwargs)

    celery_app = Celery(app.name)
    celery_app.config_from_object(app.config["CELERY"])
    celery_app.set_default()
    app.extensions["celery"] = celery_app
    celery_app.Task = FlaskTask
    return celery_app

celery_app = celery_init_app(app)

from app import routs