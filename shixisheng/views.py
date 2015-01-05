#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render_to_response,redirect
import datetime
from django.template.response import TemplateResponse as TR 
from shixisheng.models import student,Image  #先导入image
def home(request):
	#return HttpResponse("dingdong" + abcd)
	d = {}
	all = student.objects.all()#全部查找
	d['all'] = all
	all_img = Image.objects.all()	#显示所有图片
	d['all_img'] = all_img
	return TR(request,"index.html",d)
def hello(request,abcd):
	#return HttpResponse("dingdong" + abcd)
	d = {"abcd":'abcd',"date":str(datetime.datetime.now())}
	all = student.objects.all()#全部查找
	d['all'] = all
	return TR(request,"boom.html",d)
def new(request):		#增加一条数据
	print request.POST
	s = student()
	s.name = request.POST["name"]
	s.address = request.POST['address']
	s.content = request.POST['content']
	s.count = 0
	s.save()
	return redirect("/hello/abcd") 
def delete(request,id):  #删除一条数据然后跳到原网址
	s = student.objects.get(id = int(id))
	s.delete()
	return redirect("/hello/abcd")
def edit_view(request,id):
	s=student.objects.get(id=int(id))
	time = datetime.datetime.now()
	d={"s":s,"t":str(time)}
	return TR(request,"edit.html",d)

def edit(request,id):    #修改数据，替换原有的数据
	s = student.objects.get(id = int(id))
	s.name = request.POST['name']
	s.address = request.POST['address']
	s.save()
	return redirect("/hello/abcd")

