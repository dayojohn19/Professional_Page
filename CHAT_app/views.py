from django.shortcuts import render

# Create your views here.

def enter_room(request,room_name):
    print(f'\n\nEntering Room{room_name}\n\n')
    return lobby(request,room_name)

def lobby(request,room_name=None):
    if room_name!=None:
        return render(request, 'CHAT_app/lobby.html',{'room_name':room_name})
    # GET IP
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    print('\n\n---------\n\nYour IP: ',ip)
    return render(request, 'CHAT_app/lobby.html')