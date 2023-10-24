from django.shortcuts import render,get_object_or_404
from .models import Module,TP, Cour, Expose
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


def module_detail(request, module_id, nom_module):
     # Combine module_id and nom_module to form a unique identifier
    module_identifier = f"{module_id}-{nom_module}"
    
    module = get_object_or_404(Module, pk=module_id)
    courses = Cour.objects.filter(module=module)
    tps = TP.objects.filter(module=module)
    exposes = Expose.objects.filter(module=module)

    context = {
        'title':module_identifier,
        'module': module,
        'courses': courses,
        'tps': tps,
        'exposes':exposes,
        'module_identifier': module_identifier,  # Pass the identifier if needed
    }
    return render(request, 'modules/detail_module.html', context)