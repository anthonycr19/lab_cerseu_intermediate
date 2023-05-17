from django.shortcuts import render


# Create your views here.
def owner_list(request):
    data_context = {
        'nombre': 'Katty Paredes',
        'edad': 24,
        'dni': 88842232,
        'pais': 'Perú'
    }

    return render(request, 'owner/owner_list.html', data_context)
