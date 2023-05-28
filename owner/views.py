from django.db.models import F, Q
from django.shortcuts import render

from owner.forms import OwnerForm
# Create your views here.
from owner.models import Owner


"""
    Requisito:
    1. Crear un registro en la BD usando la ORM de Django que contenga.
    nombre, apellido, edad, dni, pais, vigente.
"""
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

    """Crear un objeto en una tabla de la BD"""
    #p = Owner(nombre="Luis Mejía", edad=22, dni="88888888", pais="España", vigente=True)
    #p.save()

    #p.nombre = "Margarita Tello"
    #p.save()

    """Obtener todos los elementos de una tabla de la BD"""

    #data_context = Owner.objects.all()

    """Filtración de datos: .filter()"""

    #data_context = Owner.objects.filter(nombre="Luis Mejía")

    """Filtración de datos con AND de SQL: .filter(   ,   )"""

    #data_context = Owner.objects.filter(nombre="Luis Mejía", edad=22)

    """Filtración de datos más precisos con: __contains"""

    #data_context = Owner.objects.filter(nombre__contains="evelin")

    """Filtración de datos más precisos con: __endswith"""

    #data_context = Owner.objects.filter(nombre__endswith="jía")

    """Obtener un solo objeto de la tabla en la BD"""

    #data_context = Owner.objects.get(dni="57932334")

    """Ordenar por cualqueir atributo o campo de la tabla"""

    #data_context = Owner.objects.order_by("nombre")
    #data_context = Owner.objects.order_by("-edad")

    """Ordenar concatenando diferentes métodos ORM's"""

    #data_context = Owner.objects.filter(nombre="Marcelo").order_by("edad")

    """Acortar datos: Obtener un rango de registro de una tabla en la BD"""

    #data_context = Owner.objects.all()[0:5]
    data_context = Owner.objects.all()

    """Eliminando un dato específicamente"""

    #data_context = Owner.objects.get(id=6)
    #data_context.delete()

    """Actualización de datos en la BD a un cierto grupo de datos o un solo registro"""

    #Owner.objects.filter(pais__startswith="Es").update(edad=25)

    """Utilizando F expressions"""

    #Owner.objects.filter(edad__lte=25).update(edad=F('edad') + 10)

    """Consultas complejas"""

    #query = Q(pais__startswith='Pe') | Q(pais__startswith='Es')
    #data_context = Owner.objects.filter(query, edad=35)

    """Negar Q"""

    #query = Q(pais__startswith='Pe') & ~Q(edad=30)
    #data_context = Owner.objects.filter(query)

    query = Q(pais__startswith='Pe') | Q(pais__startswith='Es')
    #data_context = Owner.objects.filter(query, edad=30)
    data_context = Owner.objects.filter(query, edad__lte=30)

    """Error de consulta con Q: no es válido"""

    #query = Q(pais__startswith='Pe') | Q(pais__startswith='Es')
    #data_context = Owner.objects.filter(edad=30, query)

    return render(request, 'owner/owner_list.html', context={'data': data_context})


def owner_search(request):

    query = request.GET.get('q', '')
    print("Query: {}".format(query))

    results = (
        Q(nombre__icontains=query)
    )
    data_context = Owner.objects.filter(results)
    #data_context = Owner.objects.filter(results).distinct()

    return render(request, 'owner/owner_search.html', context={'data': data_context, 'query': query})


def owner_details(request):
    """Obtiene todos los elementos de una tabla de la BD"""
    owners = Owner.objects.all()

    return render(request, 'owner/owner_details.html', context={'data': owners})


def owner_create(request):
    form = OwnerForm(request.POST)

    if form.is_valid():
        nombre = form.cleaned_data['nombre']
        edad = form.cleaned_data['edad']
        pais = form.cleaned_data['pais']

        form.save()

    else:
        form = OwnerForm()

    return render(request, 'owner/owner_create.html', {'form': form})


