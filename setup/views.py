from django.shortcuts import render

def custom_400_view(request, exception):
    context = {
        'title': 'Cupagis Umab',
      
    }
    return render(request, 'Cupagis_system/error.html',context, status=400)

def custom_403_view(request, exception):
    context = {
        'title': 'Cupagis Umab',
      
    }
    return render(request, 'Cupagis_system/error.html',context, status=403)

def custom_404_view(request, exception):
    context = {
        'title': 'Cupagis Umab',
      
    }
    return render(request, 'Cupagis_system/error.html',context, status=404)

def custom_500_view(request, exception):
    context = {
        'title': 'Cupagis Umab',
      
    }
    return render(request, 'Cupagis_system/error.html',context, status=500)