from django.shortcuts import render

# Create your views here.
def A2_First(request):
    return render(request,'A2_First.html')

def A2_Second(request):
    return render(request,'A2_Second.html')
    