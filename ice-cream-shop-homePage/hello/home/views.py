from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    context = {
        "variable":"AVINASH"
    }
    return render(request,'index.html',context)
    # return HttpResponse("This is Home page")

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def contact(request):
    return render(request,'contact.html')
