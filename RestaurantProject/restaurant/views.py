from django.shortcuts import render, redirect
from .models import Dish
from .forms import DishForm
from django.views.generic.edit import UpdateView

# Create your views here.

def home(request):
    return render(request,"home.html")

def menu(request):
    query = request.GET.get("q")
    if query:
        dishes = Dish.objects.filter(name__icontains=query)
    else:
        dishes = Dish.objects.all()

    dishes = dishes.select_related("category").order_by("category","name")
    return render(request,"menu.html",{"dishes": dishes})

def about(request):
    return render(request, "about.html")

def add_dish(request):
    if request.method == "POST":
        form = DishForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("menu")
    else:
        form = DishForm()

    return render(request, "add_dish.html", {"form": form})

class EditDish(UpdateView):
    model = Dish
    form_class = DishForm
    template_name = "edit_dish.html"
    success_url = "/menu/"

def delete_dish(request, pk):
    dish = Dish.objects.get(pk=pk)

    if request.method == "POST":
        dish.delete()
        return redirect("menu")

    return render(request, "delete_dish.html",{"dish":dish})
