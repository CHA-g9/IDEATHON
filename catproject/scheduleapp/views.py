from django.shortcuts import redirect, render, get_object_or_404
from .models import schedule as Event

# Create your views here.
def schedule_home(request):
    whole_schedules = Event.objects.all()
    return render(request, "schedules.html", {'schedules':whole_schedules})

def new_schedule(request):
    return render(request, "create.html")

def create_schedule(request):
    new_event = Event()
    new_event.event_name = request.POST['event_name']
    new_event.event_date = request.POST['event_date']
    new_event.event_place = request.POST['event_place']
    new_event.save()
    return redirect('schedule')

def edit_schedule(request, id):
    edit_event = Event.objects.get(id = id)
    return render(request, 'edit.html', {'edit_event' : edit_event})

def update_schedule(request, id):
    update_event = Event.objects.get(id = id)
    update_event.event_name = request.POST['event_name']
    update_event.event_date = request.POST['event_date']
    update_event.event_place = request.POST['event_place']
    update_event.save()
    return redirect('schedule')