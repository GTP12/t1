from django.shortcuts import render
app_name = 'transaction'
def index(request):
    return render(request,'index.html')

def person_center(request):
    return render(request,'center.html')
