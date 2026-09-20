from typing import List

from fastapi import APIRouter, HTTPException

from models.task import Task, TaskOut


router = APIRouter(prefix="/tasks", tags=["tasks"])

tasks: List[Task] = []
next_id = 1


@router.get("", response_model=List[TaskOut])
def get_tasks():
    return tasks


@router.post("", response_model=TaskOut)
def create_task(task: Task):
    global next_id

    task.id = next_id
    next_id += 1
    tasks.append(task)
    return task


@router.get("/{task_id}", response_model=TaskOut)
def get_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task

    raise HTTPException(status_code=404, detail="Задача не найдена")
