from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'baseapp/index.html')


def addcase(request):
    return render(request,'baseapp/addcase.html')