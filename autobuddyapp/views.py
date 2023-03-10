from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import ModelCreationForm
from .models import Make, Model, Car


def model_create_view(request):
    form = ModelCreationForm()
    if request.method == 'POST':
        form = ModelCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('model_add')
    return render(request, 'models/home.html', {'form': form})


def model_update_view(request, pk):
    car = get_object_or_404(Car, pk=pk)
    form = ModelCreationForm(instance=car)
    if request.method == 'POST':
        form = ModelCreationForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('model_change', pk=pk)
    return render(request, 'models/home.html', {'form': form})


# AJAX
def load_models(request):
    make_id = request.GET.get('make_id')
    models = list(Model.objects.filter(make__id = make_id).values())
    return JsonResponse({'models': models})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)

def load_about(request):
    return render(request, 'models/about_autobuddy.html')

def load_autobuddy_estimator(request):
    return render(request, 'models/autobuddy_estimator.html')

def load_is_it_fair(request):
    return render(request, 'models/is_it_fair.html')

def load_make_a_report(request):
    return render(request, 'models/make_report.html')