from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts =[
    {
        "author": "Can",
        "title": "My Post",
        "content": "My First Post",
        "datePosted": "27 February 2024"
    },
    {
        "author": "Ada",
        "title": "Her Post",
        "content": "Her First Post",
        "datePosted": "28 February 2024"
    }
    
]



def home(request):
    
    context = {
        "posts": posts
    }
    
    return render(request, "blog/home.html", context)

def about(request):
    return render(request, "blog/about.html", {"title": "About"})