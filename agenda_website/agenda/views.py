from django.shortcuts import render
from .models import AgendaItem

def agenda_view(request):
    items = AgendaItem.objects.all()
    return render(request, 'agenda_website/agenda.html', {'items': items})