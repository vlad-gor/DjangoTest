from django.shortcuts import render

# Create your views here.
def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        
    return render(request, 'index.html')