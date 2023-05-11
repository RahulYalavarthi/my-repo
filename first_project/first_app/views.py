from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request) :    # 'request' name is convention. It can be some other name too.
    return HttpResponse("<h1>Hello World</h1>")
def other(request) :    # 'request' name is convention. It can be some other name too.
    return HttpResponse("<h2>chesesav le</h2>")
def index(request) :
  my_dict = { 'message' : "This is an injected content"}
  return render(request,'index.html',context=my_dict)
clicked = 1
def index(request) :
  global clicked
  clicked += 1
  my_dict = {'count' : clicked}
  return render(request, 'index.html', my_dict)

def help(request):
    return render(request, "help.html")
