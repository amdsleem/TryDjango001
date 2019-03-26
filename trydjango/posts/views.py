from urllib.parse import quote_plus

from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
import random
from .forms import PostForm

# Create your views here.
from .models import Post

def post_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    # if not request.user.is_authenticated:     #this block same that one above
    #     raise Http404
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
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
    instance = get_object_or_404(Post, id=id)
    if instance.publish > timezone.now().date() or instance.draft:
        if not request.user.is_staff or not request.user.is_superuser:
            raise Http404
    share_string = quote_plus(instance.content)
    context = {
        "title": instance.title,
        "instance": instance,
        "share_string": share_string
    }
    return render(request, "post_detail.html", context)

def post_list(request):  #list items
    today = timezone.now().date()
    queryset_list = Post.objects.active()  #.order_by("-timestamp") #now I can hidden future posts
    #filter(draft=False).filter(publish__lte=timezone.now()) #this cutted befor all()
    if request.user.is_staff or request.user.is_superuser:
        queryset_list = Post.objects.all()
    
    query = request.GET.get("q") #this line and next line of 'if' make dinamich search
    if query:
        queryset_list = queryset_list.filter(
            Q(title__icontains=query) | #( | == or )
            Q(content__icontains=query) |
            Q(user__first_name__icontains=query) |
            Q(user__last_name__icontains=query)
        ).distinct()
    paginator = Paginator(queryset_list, 2) # Show 25 contacts per page
    page_request_var = 'sf7a'
    page = request.GET.get(page_request_var)
    queryset = paginator.get_page(page)
    context = {
        "object_list": queryset,
        "title": "List",
        "page_request_var": page_request_var,
        "today": today
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
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
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
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, "Successfully Deleted")
    return redirect("post:list")
