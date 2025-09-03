from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406496321',
        'name': 'Michael Stephen Daniel Panjaitan',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)
