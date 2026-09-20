from typing import Optional

from pydantic import BaseModel, field_validator


class Category(BaseModel):
    name: str
    color: str


class Task(BaseModel):
    id: Optional[int] = None
    title: str
    description: str
    is_completed: bool = False
    category: Category
    internal_note: str = "Служебная заметка"

    @field_validator("title")
    def check_title_length(cls, value):
        if len(value.strip()) < 3:
            raise ValueError("Название задачи должно содержать минимум 3 символа")
        return value


class TaskOut(BaseModel):
    id: int
    title: str
    description: str
    is_completed: bool
    category: Category
