from django.shortcuts import render
def geeks_view(request):
    context={"data":'vinoth kumar'}
    return render(request,'app/template1.html',context)
def nav_view(request):
    context={'etho':"https://pypi.org/project/pyetho/"}   ----# this link is to navigate to my core project
    return render (request,'app/nav.html',context)   
