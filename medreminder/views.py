from django.shortcuts import render, get_object_or_404, redirect
from .models import Reminder
from .forms import ReminderForm

def reminder_list(request):
    reminders = Reminder.objects.all()
    return render(request, 'medreminder/reminder_list.html', {'reminders': reminders})

def reminder_detail(request, pk):
    reminder = get_object_or_404(Reminder, pk=pk)
    return render(request, 'medreminder/reminder_detail.html', {'reminder': reminder})

def reminder_create(request):
    if request.method == 'POST':
        form = ReminderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reminder_list')
    else:
        form = ReminderForm()
    return render(request, 'medreminder/reminder_form.html', {'form': form})

def reminder_update(request, pk):
    reminder = get_object_or_404(Reminder, pk=pk)
    if request.method == 'POST':
        form = ReminderForm(request.POST, instance=reminder)
        if form.is_valid():
            form.save()
            return redirect('reminder_list')
    else:
        form = ReminderForm(instance=reminder)
    return render(request, 'medreminder/reminder_form.html', {'form': form})

def reminder_delete(request, pk):
    reminder = get_object_or_404(Reminder, pk=pk)
    if request.method == 'POST':
        reminder.delete()
        return redirect('reminder_list')
    return render(request, 'medreminder/reminder_confirm_delete.html', {'reminder': reminder})
