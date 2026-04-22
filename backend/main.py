from fastapi import FastAPI
from schemas.task import Task


app = FastAPI()


# Get All Tasks
@app.get("/tasks")
def get_taks():
    return{"message":" Show All Tasks here"}

# Get One Task by Id
@app.get("tasks/id")
def get_task(id:int):
    return{"message":f"Show tasks by id {id}"}

# create Tasks
@app.post("/tasks")
def create_task(t:Task):
    return {"message":f"task {t} received"}

# Update Tasks
@app.put("/tasks/id")
def update_task(id:int,t:Task):
    return {"message":f"Taks {id} Updated  successfully , New task {t} "}


# Delete Tasks
@app.delete("/tasks/id")
def delete_task(id:int):
    
    return {"message":f"Task {id} Deleted successfully"}
