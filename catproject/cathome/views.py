from django.shortcuts import render, get_object_or_404
from scheduleapp.models import schedule

# Create your views here.
def base(request):
    return render(request, "CAT_HOME.html")

def show(request, id):
    show_events = schedule.objects.get(id=id)
    return render(request, "CAT_HOME.html", {'show_events': show_events})
