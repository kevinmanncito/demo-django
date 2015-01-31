from django.shortcuts import render
from .models import TimeEntry


def home(request):
    if not request.user.is_anonymous():
        entries = TimeEntry.objects.filter(user=request.user)
    else:
        entries = TimeEntry.objects.all()
    return render(request, 'home.html', {'entries': entries})

def entries(request, entry_id):
    entry = TimeEntry.objects.get(id=entry_id)
    return render(request, 'entry.html', {'entry': entry})