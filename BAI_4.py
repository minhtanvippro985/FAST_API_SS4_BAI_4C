from fastapi import FastAPI
from pydantic import BaseModel,Field
from typing import Optional

EMAIL_REGEX = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
PHONE_REGEX = r"^0[0-9]{9}$"

class Student_schema(BaseModel):
    full_name:str = Field(... , min_length=3)
    email:str = Field(pattern=EMAIL_REGEX)
    age:int = Field(... , gt= 18 , lt= 120)
    course:Optional[str] = None
    phone: Optional[str] = Field(None, pattern=PHONE_REGEX)
    


student_list = [
{
  "full_name": "Nguyen Van A",
  "email": "existing@gmail.com",
  "age": 20,
  "course": "python",
  "phone": "0987654321"
},
]

app = FastAPI()


@app.post("/students")
def add_new_student(student:Student_schema):
    new_student = {
            "full_name" : student.full_name,
            "email" : student.email,
            "age" : student.age,
            "course" : student.course,
            "phone" : student.phone
        }
    for student in student_list:
        if student['email'] == new_student['email']:
            return{
                "detail": "Email đã tồn tại trong hệ thống"
            }


    student_list.append(new_student)
    return{
        "message" : "thêm sinh viên thành công",
        "data" : student_list
    }
