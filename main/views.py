from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406432482',
        'name': 'Moch Raydzan',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)