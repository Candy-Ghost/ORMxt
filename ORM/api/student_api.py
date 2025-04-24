from wsgiref.validate import validator
from typing import List
from fastapi import APIRouter
from models import *
from pydantic import BaseModel, field_validator
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi.exceptions import HTTPException
from fastapi.middleware.cors import CORSMiddleware
student_api=APIRouter()





@student_api.get("/",description="这是一个演示 FastAPI 接口注释的示例", summary="获取all信息",)
async def getallstudent():
    # Students= await student.all()
    # print(Students)


#过滤查询 filter
    # Students = await student.filter(name="张三")
#过滤查询 get：返回数据模型
    # Stu = await student.filter(name="张三") #[<student()>]
    #print(Stu[0].name )
    # Students = await student.get(name="张三")    #<student()>
    # print(Students.name)

#模糊查询
    # Stu = await student.filter(sno__gt=19250118)#查询sno中大于19250118的信息
    # Stu = await student.filter(sno__lt=19250118)  # 查询sno中小于19250118的信息
    # Stu = await student.filter(sno__range=[1,19250120]  # 查询sno中1到19250120的信息
    # Stu = await student.filter(sno__in=[1,19250120]  # 查询sno中1和19250120的信息
#values查询
    # Students = await student.all().values("name","sno") #[{},{},{}]只会得到name这一列
    # return {
    #     "操作":Students
    # }
#一对多查询
    Students = await student.get(name="张三")  # student()
    print(Students .name)
    print(await Students.clas.values("classname"))
    studentddd=await student.all().values("name","clas__classname") #
    print(await Students.cours.all().values("name"))
    return studentddd


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

@student_api.get("/one",)
def getoenstudent(id:int):
    return {
        "操作":f"返回学生{id}的信息"
    }
#
class studentin(BaseModel):

    name :str
    password : int
    sno : int
    # 一对多
    clas_id :int
    # 多对多
    Coursss: List[int]=[]
#
#
    # @field_validator('name')
    # def name_must_contain_space(cls, value: str) -> str:
    #     if value bot:
    #         raise ValueError("Name must contain a space")
    #     return value.title()  # 可以修改值

    @field_validator("sno")
    def name_must_contain_space(cls, value: int) ->int:
        if not (19250000 < value < 19250999):
            raise ValueError( "学号要在19250000-19250998之间")
        return value # 可以修改值

class studentout(BaseModel):
    name :str
    password : int
    sno : int
     # 一对多
    clas_id :int


@student_api.post("/id")
async def addoenstudent(student_in:studentin):
    #方法1
    # STudent=student(name=student_in.name,password=student_in.password,sno=student_in.sno,clas_id=student_in.clas_id)
    # await STudent.save()
#方法2
    STudent = await student.create(name=student_in.name, password=student_in.password, sno=student_in.sno,clas_id=student_in.clas_id)
    choose_cours= await Course.filter(id__in=student_in.Coursss)
    await student.cours.add(*choose_cours)
    return {
        "操作":"增加学生的信息"
    }

@student_api.get("/{id_one}")
async def getonestudent(id_one:int):
    onestudent= await student.get(id=id_one)

    return onestudent


@student_api.put("/{student_id}")
async def upstudent(student_id:int,student_in:studentout):
        data=student_in.dict()
        print(data)
        await student.filter(id=student_id).update(**data)#注意字段和数据库一致才可以查询

        return {
            "操作":f"更新id={student_id}"
        }
@student_api.delete("/{student_id}")
async def destdent(student_id:int):
    deletetestudent= await student.filter(id=student_id).delete()
    if not deletetestudent:
        raise HTTPException(status_code=404,detail=f"主键为{student_id}的学生没删除")
    return {}