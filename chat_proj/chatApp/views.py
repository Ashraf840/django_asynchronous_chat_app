from django.shortcuts import render
# from django.http import HttpResponse

def index(request):
    # return HttpResponse("Home Page")
    # Need to set "ASGI_APPLICATION" in the "settings.py" file run the server, since "channels" are installed
    context = {}
    return render(request, 'index.html', context)

# the "room_name" is coming from the URL, which is first input inside the browser's URL, then hits back to the "urls.py", then passed inside this func's param
def room(request, room_name):
    context = {
        'room_name': room_name,
    }
    return render(request, 'chat_room.html', context)