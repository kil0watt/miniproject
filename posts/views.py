from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from . models import Post 

from . forms import PostForm

def post_home(request):
	return HttpResponse("<h1>Hello</h1>")


def post_create(request):
	form= PostForm(request.POST or None)
	if form.is_valid():
		instance= form.save(commit=False)
		instance.save()
		messages.success(request, "Successfully Created")
		return HttpResponseRedirect(instance.get_absolute_url())
		
	context={
		"form" : form
	}
	return render(request,"post_form.html",context)

def post_detail(request,id):
	instance = get_object_or_404(Post,id=id)
	context ={
		"instance" : instance
	}
	return render(request,"post_detail.html",context)

def post_list(request):
	objects = Post.objects.all()
	context= {
		"object_list" : objects,
		"title" : "list"
	}
	return render(request,"post_list.html",context)

def post_update(request,id=None):
	instance = get_object_or_404(Post,id=id)
	form= PostForm(request.POST or None,instance=instance)
	if form.is_valid():
		instance= form.save(commit=False)
		instance.save()
		messages.success(request, "Successfully updated")
		return HttpResponseRedirect(instance.get_absolute_url())	
	context ={
		"instance" : instance,
		"form" : form
	}
	return render(request,"post_form.html",context)

def post_delete(request,id=None):
	instance = get_object_or_404(Post,id=id)
	instance.delete()
	messages.success(request, "Successfully deleted")

	return redirect("posts:list")