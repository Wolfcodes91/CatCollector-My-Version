from dataclasses import fields
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Cat, Toy
from .forms import FeedingForm
# Create your views here.

def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cats_index(request):
    cats = Cat.objects.all()
    return render(request, 'cats/index.html', {'cats': cats})

def cats_detail(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    #instantiate FeedingForm to be rendered within 
    # the detail.html template
    feeding_form = FeedingForm()
    return render(request, 'cats/detail.html', {
    'cat': cat,
    'feeding_form': feeding_form,
  })

#Class based view
class CatCreate(CreateView):
  model = Cat
  fields = '__all__'

class CatUpdate(UpdateView):
  model = Cat
  fields = ['breed', 'description', 'age']

class CatDelete(DeleteView):
  model = Cat
  success_url = '/cats/'

def add_feeding(request, cat_id):
  # create a ModelForm instance using the data in request
  form = FeedingForm(request.POST)
  # check if form is valid
  if form.is_valid():
    # dont want to try to save the feeding 
    #until the cat_id has been assigned
    new_feeding = form.save(commit=False)
    new_feeding.cat_id = cat_id
    new_feeding.save()
  return redirect('detail', cat_id=cat_id)

class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'
  success_url = '/toys_index/'

def toys_index(request):
    toys = Toy.objects.all()
    return render(request, 'toys_index.html', {'toys': toys})

def toys_detail(request, toy_id):
    toy = Toy.objects.get(id=toy_id)
    return render(request, 'toys_detail.html', {
    'toy': toy,
  })

class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys_index/'