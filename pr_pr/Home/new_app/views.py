from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    context = {
        'variable1': 'this is sent',
        'variable2': 'value sent'
    }
    return render(request, 'index.html',context)
    # return HttpResponse('this is my page')

def about(request):
    return HttpResponse('this is about page')    

def services(request):
    return HttpResponse('this is service page')        

def contact(request):
    return HttpResponse('this is contact page')        