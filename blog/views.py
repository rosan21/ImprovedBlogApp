from django.shortcuts import render

posts = [
    {
        'author':'Roshan Gurung',
        'title' : 'Blog Post 1',
        'date_posted' : '2022 April 22',
        'content': 'Hello Nepal Dai '
    },
    {
        'author':'Roshan Gurung',
        'title' : 'Apple Ball 2',
        'date_posted' : '2022 April 22',
        'content': 'Hello Nepal Dai '
    }
]

# Create your views here.
def home(request):
    return render(request, 'home.html', {'posts':posts})

def about(request):
    return render(request,'about.html')