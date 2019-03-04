from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
import random
from .forms import PostForm

# Create your views here.
from .models import Post

def post_create(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        # message success
        messages.success(request, "Successfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form,
    }
    return render(request, "post_form.html", context)


'''
    # if request.method == "POST":
    #     print(request.POST.get("content"))
    #     print(request.POST.get("title"))
    #     Post.objects.create(title=title)
'''

def post_detail(request, id=None):  #retrieve
    # instance = Post.objects.get(id=1)
    # a = list(range(7,16))
    instance = get_object_or_404(Post, id=id) #id=random.choice(a))
    context = {
        "title": instance.title,
        "instance": instance
    }
    return render(request, "post_detail.html", context)

def post_list(request):  #list items
    queryset_list = Post.objects.all()  #.order_by("-timestamp")
    paginator = Paginator(queryset_list, 5) # Show 25 contacts per page
    page_request_var = 'sf7a'
    page = request.GET.get(page_request_var)
    queryset = paginator.get_page(page)
    context = {
        "object_list": queryset,
        "title": "List",
        "page_request_var": page_request_var
    }
    return render(request, "post_list.html", context)
    # return HttpResponse("<h1>List</h1>")


'''
    if request.user.is_authenticated:
        context = {
            "title": "My User List"
        }
    else:
        context = {
            "title": "List"
        }
'''


def post_update(request, id=None):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        # message success
        messages.success(request, "<a href='#'>Item</a> Saved", extra_tags="html_safe")
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "title": instance.title,
        "instance": instance,
        "form": form,
    }
    return render(request, "post_form.html", context)
 


def post_delete(request, id=None):
        instance = get_object_or_404(Post, id=id)
        instance.delete()
        messages.success(request, "Successfully Deleted")
        return redirect("post:list")