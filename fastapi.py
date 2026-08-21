from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Student API is running"}

@app.get("/student/{name}")
def get_student(name: str):
    return {
        "student_name": name,
        "course": "CSE",
        "status": "Active"
    }

@app.get("/result/{marks}")
def check_result(marks: int):

    if marks >= 40:
        result = "PASS"
    else:
        result = "FAIL"

    return {
        "marks": marks,
        "result": result
    }