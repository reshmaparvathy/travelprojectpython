from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def demo(request):
    return render(request,"index.html")

def Arithmetic_operation(request):
    x=int(request.GET['num1'])
    y=int(request.GET['num2'])
    add=x+y
    sub=x-y
    mul=x*y
    div=x/y


    return render(request,"result.html",{'result1':add,'result2':sub,'result3':mul,'result4':div})
# def home(request):
#     return HttpResponse("am home page")
#
# def about(request):
#     return render(request,"about.html")
#
# def contact(request):
#     return render(request,"contact.html")
#
# def detail(request):
#     return render(request,"detail.html")
#
# def thank(request):
#     return render(request,"thank.html")