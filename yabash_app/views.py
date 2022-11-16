from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'yabash_app/index.html')
