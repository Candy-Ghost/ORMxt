from tortoise.models import Model
from tortoise import fields

class student(Model):
        id = fields.IntField(pk=True)
        name = fields.CharField(max_length=50,description="姓名")
        password = fields.CharField(max_length=50,description="密码")
        email = fields.CharField(max_length=100, unique=True,description="邮件")
        sno = fields.IntField(description="学号")
        created_at = fields.DatetimeField(auto_now_add=True)


        #一对多
        clas=fields.ForeignKeyField("models.Clas",related_name="student")
        # 多对多
        Cours=fields.ManyToManyField("models.Course",related_name="student")

class Course(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=50, description="课程名称")
    teacher=fields.ForeignKeyField("models.Teacher",related_name="teacher")


class Clas(Model):
     id = fields.IntField(pk=True)
     classname = fields.CharField(max_length=50, description="班级名称")
     arr = fields.CharField(max_length=50, description="地址")

class Teacher(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=50, description="老师姓名")
    password = fields.CharField(max_length=50, description="老师密码")
    tsno = fields.IntField(description="老师工号")