from django.shortcuts import render

# Create your views here.

def rooms(request):
    rooms=Room.objects.all()
    return render(request, "home.html", {
        "rooms": rooms
    })
