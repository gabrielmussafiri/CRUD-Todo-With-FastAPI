from fastapi import FastAPI
from schemas.task import Task


app = FastAPI(title="Task Management API", description=
              """
              This App will Allow you to :
              - List all Your Task
              - Get The details of all the task
              - Add a New Task
              - Update a Task 
              _ Delete a Task
              
              """)


# Get All Tasks
@app.get("/tasks", summary=" Get All Tasks",description="All Tasks in DB is in Json" , response_description="The response is in JSon Format")
def get_taks():
    return{"message":" Show All Tasks here"}

# Get One Task by Id
@app.get("tasks/id", summary="Get Task by Id")
def get_task(id:int):
    return{"message":f"Show tasks by id {id}"}

# Create Tasks
@app.post("/tasks", summary='Create a New Task')
def create_task(t:Task):
    return {"message":f"task {t} received"}

# Update Tasks
@app.put("/tasks/id", summary="Update Task")
def update_task(id:int,t:Task):
    return {"message":f"Task {id} Updated  successfully , New task {t} "}


# Delete Tasks
@app.delete("/tasks/id", summary=" Delete Task")
def delete_task(id:int):
    
    return {"message":f"Task {id} Deleted successfully"}
