import logging

from celery.app.log import TaskFormatter
from celery.signals import after_setup_task_logger

from app import celery, create_app

app = create_app()
app.app_context().push()


@after_setup_task_logger.connect
def setup_task_logger(logger, *args, **kwargs):
    sh = logging.handlers.RotatingFileHandler(
        app.config['LOG_CELERY_FILE'],
        maxBytes=app.config['CELERY_LOGGING']['maxBytes'],
        backupCount=app.config['CELERY_LOGGING']['backupCount']
    )
    sh.setFormatter(
        TaskFormatter(
            app.config['CELERY_LOGGING']['format']))
    logger.setLevel(logging.INFO)
    logger.addHandler(sh)
