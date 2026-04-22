from pydantic import BaseModel , Field
from enum import Enum


class State(str,Enum):
    TODO ='Todo',
    INPROGRESS ='In Progress'
    DONE ='Done'
class Task(BaseModel):
    title : str = Field(min_length=1)
    description : str = Field(min_length=1)
    state : State
    