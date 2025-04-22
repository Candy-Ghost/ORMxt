from wsgiref.validate import validator
from typing import List
from fastapi import APIRouter
from models import *
from pydantic import BaseModel, field_validator
from fastapi.templating import Jinja2Templates
from fastapi import Request

student_api=APIRouter()


@student_api.get("/")
async def getallstudent():
    # Students= await student.all()
    # print(Students)


#过滤查询 filter
    # Students = await student.filter(name="张三")
#过滤查询 get：返回数据模型
    # Stu = await student.filter(name="张三") #[student()]
    #print(Stu[0].name )
    # Students = await student.get(name="张三")    #student()
    # print(Students.name)

#模糊查询
    # Stu = await student.filter(sno__gt=19250118)#查询sno中大于19250118的信息
    # Stu = await student.filter(sno__lt=19250118)  # 查询sno中小于19250118的信息
    # Stu = await student.filter(sno__range=[1,19250120]  # 查询sno中1到19250120的信息
    # Stu = await student.filter(sno__in=[1,19250120]  # 查询sno中1和19250120的信息
#values查询
    Students = await student.all().values("name","sno") #[{},{},{}]只会得到name这一列
    return {
        "操作":Students
    }
#
@student_api.get("/index.html")
async def indexstudent(request:Request):
    templats=Jinja2Templates(directory="templats")
    Students = await student.all()
    return templats.TemplateResponse(
        "index.html",{
            'request':request,
            "students":Students
        }
    )

@student_api.get("/one")
def getoenstudent(id:int):
    return {
        "操作":f"返回学生{id}的信息"
    }
#
class studentin(BaseModel):

    name :str
    password : int
    email : str
    sno : int
    # 一对多
    clas_id :int
    # 多对多
    Cours : List[int]=[]
#
#
    # @field_validator('name')
    # def name_must_contain_space(cls, value: str) -> str:
    #     if value bot:
    #         raise ValueError("Name must contain a space")
    #     return value.title()  # 可以修改值

    @field_validator("sno")
    def name_must_contain_space(cls, value: str) -> str:
        if not (19250000 < value < 19250999):
            raise ValueError("Name must contain a space")
        return value # 可以修改值

    # @field_validator("sno")
    # def sno_validator(cls, value):
    #      value>19250000 and value<19250999, "学号要在19250000-19250998之间"
    #      return value
#
@student_api.post("/id")
async def addoenstudent(student_in:studentin):
    STudent=student(name=student_in.name,password=student_in.password,email=student_in.email,sno=student_in.sno,clas_id=student_in.clas_id)
    await STudent.save()
    return {
        "操作":"增加学生的信息"
    }