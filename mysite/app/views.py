from django.shortcuts import render
from app.models import Measure

def measures(request):
    context = {
        "measures": Measure.objects.all()
    }
    return render(request=request, context=context, template_name='measures.html')
