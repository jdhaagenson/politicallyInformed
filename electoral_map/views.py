from django.shortcuts import render


# Create your views here.
def map_view(request):
    return render(request, 'electoral_map.html')