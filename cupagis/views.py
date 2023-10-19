from django.shortcuts import render
from .models import Module
from django.db.models import Q


def liste_modules(request):
    # Initial query with all modules
    modules = Module.objects.all()

    # Handling search by nom_Module
    search_query = request.GET.get('search', '')  # Get the search query from the URL parameters
    if search_query:
        # Filter modules that contain the search query in nom_Module
        modules = modules.filter(nom_Module__icontains=search_query)

    # Handling filtering by niveau
    niveau_filter = request.GET.get('niveau', '')
    if niveau_filter:
        # Filter modules by niveau
        modules = modules.filter(niveau=niveau_filter)

    # Handling filtering by semestre
    semestre_filter = request.GET.get('semestre', '')
    if semestre_filter:
        # Filter modules by semestre
        modules = modules.filter(semestre=semestre_filter)

    context = {
        'title': 'Cupagis Umab',
        'modules': modules,
    }
    return render(request, 'Cupagis_system/layout.html', context)
