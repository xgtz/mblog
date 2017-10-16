# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from models import Post

# Create your views here.
def homepate(request):
	posts=Post.objects.all()
	post_lists=list()
	for index,post in enumerate(posts):
		post_lists.append("No.".format(str(index)) + str(post) +"<br>") 
	
	return HttpResponse(post_lists)