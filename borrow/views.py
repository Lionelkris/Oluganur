from django.shortcuts import render, redirect
from django.http import HttpResponse
from users.forms import ExampleForm
from users.models import UserRequestProfile
from .models import LenderPreferences


def home(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            print(form_data)
            list_of_lenders = LenderPreferences.objects.filter(machine_vehicle_purchase=form_data['machine_vehicle_purchase'])
            print(list_of_lenders)
            return render(request, 'borrow/lender_list.html', {'list_of_lenders': list_of_lenders})
    else:
        form = ExampleForm()
    return render(request, 'borrow/home.html', {'form': form})


def about(request):
    return render(request, 'borrow/about.html')

