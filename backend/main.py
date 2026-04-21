from fastapi import FastAPI


app = FastAPI()


@app.get("/tasks")
def get_taks():
    return{"message":" All Tasks here"}

@app.get("tasks/id")
def get_task(id:int):
    return{"message":f"get tasks by id {id}"}