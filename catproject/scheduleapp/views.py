from django.shortcuts import redirect, render, get_object_or_404
from .models import schedule as Event

# Create your views here.
def base(request):
    return render(request, 'MAIN.html')

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

def show_schedule(request, event_date):
    whole_schedules = Event.objects.all()
    date = event_date
    show_event = Event.objects.get(event_date = date)
    show_date = show_event.event_date
    show_date_id = str(show_date)[8:10]
    show_name = show_event.event_name
    show_time = str(show_date)[11:16]
    return render(request, "home.html", {"schedules":whole_schedules, "show_date":show_date, "show_date_id": show_date_id, "show_name":show_name, "show_time" : show_time})


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

def delete(request, id):
    delete_schedule = Event.objects.get(id = id)
    delete_schedule.delete() # delete 메서드
    return redirect('schedule')


def welcome(request):
    return render(request, "CAT_HOME.html")

def account_book(request):
    return render(request, "account_book.html")

def to_do_list(request):
    return render(request, "to_do_list.html")

def hello_world(request):
    
    if request.method == "POST":
        temp = request.POST.get("hello_world_input")

        return render(request, 'account_book.html', context = {'text':temp})

    else:
        return render(request, 'account_book.html', context = {'text':'GET'})