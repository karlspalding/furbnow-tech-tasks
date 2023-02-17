from django.shortcuts import render


def measures(request):
    return render(request=request, template_name='measures.html')