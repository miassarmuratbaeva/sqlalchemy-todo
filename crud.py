from sqlalchemy import (
    insert, select, update, delete
)
from database import engine
from tables import tasks_table


def create_task(title: str, description: str | None = None):
    pass

def get_tasks():
    pass

def update_task(pk: int, title: str | None = None, description: str | None = None):
    pass

def delete_task(pk: int):
    pass

def change_task_status(pk: int):
    pass
