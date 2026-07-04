from pydantic import BaseModel,EmailStr,Field
from typing import Optional

class Student(BaseModel):
   # name : str
   name : str='sahil'
   age : Optional[int]=None
#   email : EmailStr
   cgpa : float=Field(gt=0,lt=10)

#new_student={"name":"sahil"}
#new_student = {'age':19}
#new_student={'email':'sahil9926@gmail.com'}
new_student={'cgpa':9}

student=Student(**new_student)

print(student)
print(student.name)