from django.shortcuts import render


def get_chat(request):
    data = {'h1': 'chat'}
    return render(request, 'chat.html', data)
