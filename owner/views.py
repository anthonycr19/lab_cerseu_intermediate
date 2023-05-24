from django.shortcuts import render


# Create your views here.
def owner_list(request):
    # data_context = {
    #     'nombre': 'Katty Paredes',
    #     'edad': 16,
    #     'dni': 88842232,
    #     'pais': 'Perú',
    #     'vigente': False
    # }

    data_context = [
        {
            'nombre': 'Katty Paredes',
            'edad': 16,
            'dni': 88842232,
            'pais': 'Perú',
            'vigente': False,
            'pokemons': [
                {
                    'nombre_pokemon': 'Charizard',
                    'ataques': ['Ataque 1 - Charizard', 'Ataque 2 - Charizard', 'Ataque 3 - Charizard']
                }
            ]
        },
        {
            'nombre': 'Miguel Valera',
            'edad': 26,
            'dni': 43452345,
            'pais': 'España',
            'vigente': False,
            'pokemons': [
                {

                }
            ]
        },
        {
            'nombre': 'Jesús de la Cruz',
            'edad': 30,
            'dni': 88842232,
            'pais': 'Colombia',
            'vigente': False,
            'pokemons': [
                {

                }
            ]
        },
        {
            'nombre': 'Liliana Vargas',
            'edad': 24,
            'dni': 85552232,
            'pais': 'España',
            'vigente': True,
            'pokemons': [
                {

                }
            ]
        }
    ]

    return render(request, 'owner/owner_list.html', context={'data': data_context})

