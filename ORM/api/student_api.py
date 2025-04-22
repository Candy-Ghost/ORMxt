from fastapi import APIRouter
from models import *

student_api=APIRouter()


@student_api.get("/")
async def getallstudent():
    Students= await student.all()
    print(Students)
    for stu in Students:
        print(stu.name,stu.sno)
    return {

        "操作":"返回所有学生的信息"
    }
#
@student_api.get("/{id}")
def getoenstudent(id:int):
    return {
        "操作":f"返回学生{id}的信息"
    }
#
# @student_api.post("/{id}")
# def addoenstudent(id:int):
#     return {
#         "操作":f"增加学生{id}的信息"
#     }