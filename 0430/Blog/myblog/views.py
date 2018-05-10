# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.shortcuts import render
from .models import Post
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from .models import *
import datetime

from django.shortcuts import render,redirect

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def add(request):
	if request.method =="POST" :
	#如果是以POST的方式才處理
		title = request.POST['title'] 
		#取得表單輸入資料
		text = request.POST['article']
		published_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		aa = Post.objects.create(title=title, text=text,published_date =published_date)
		aa.save()
		return redirect('/post_list')

	return render(request,'blog/add.html', locals())#在blog資料夾裡 所以要加blog/

def edit(request):
#抓序號？
	pk = request.GET.get('q')
	post = Post.objects.get(pk=pk)
	if request.method == 'POST':
		post.title = request.POST.get('edittitle')
		post.text = request.POST.get('edittext')
		post.save()
		return redirect('/post_list')
	return render(request, 'blog/edit.html', {'post': post})


def delete(request):                  #刪除資料
    if request.method == "POST":  #如果是以POST的分是才處理
        id = request.GET.get('a')  #取得表單輸入的編號
        unit = Post.objects.get(id=id)  #取得id欄位的資料
        unit.delete()                      #刪除資料
        return redirect('/post_list')

    return render(request,"blog/delete.html")









