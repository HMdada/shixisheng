#coding:utf-8
from django.db import models


class Image(models.Model): 
	img = models.ImageField(upload_to = './img')  #图片的控件，把图片存到这个目录下
class student(models.Model):
	name = models.CharField(max_length=30)
	address  = models.CharField(max_length=50)
	count = models.IntegerField(default = 0)#可以写默认值，访问量
	date = models.DateField(auto_now=True)  #自动保存时间到auto
	content = models.TextField()  #文本类型，大的输入框

