from celery import Celery

# Create a Celery instance
app = Celery('tasks', 
             broker='redis://localhost:6379/0',
             backend='db+sqlite:///results.db')

# Example configuration
app.conf.update(
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='UTC',
    enable_utc=True,
)

@app.task
def add(x, y):
    return x + y