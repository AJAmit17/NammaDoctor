from django.shortcuts import render, redirect
from .models import Remedies
from .forms import RemedyForm
from django.core.paginator import Paginator

def remedy_list(request):
    remedies = Remedies.objects.all()
    paginator = Paginator(remedies, 3)  # Show 10 remedies per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'remedies/list.html', {
        'remedies': page_obj,
        'title': 'Remedies List'
    })

def add_remedy(request):
    if request.method == 'POST':
        form = RemedyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Saves to the primary database
            return redirect('remedy_list')
    else:
        form = RemedyForm()
    return render(request, 'remedies/user_remedies.html', {
        'form': form,
        'title': 'Add remedies'
        })
