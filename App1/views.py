from django.shortcuts import render

# Create your views here.
def A1_First(request):
    return render(request,'A1_First.html')

def A1_Second(request):
    return render(request,'A1_Second.html')