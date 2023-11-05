from django.shortcuts import render, redirect
from django.http import HttpRequest
from item.models import Items, Categories
from .forms import SignUpForm


def home(request:HttpRequest):
    items = Items.objects.filter(sold=False)
    categories = Categories.objects.all()
    categories_items_amount = [category.items.filter(sold=False).count() for category in categories]

    return render(request, "core/home.html",{
        "categories":zip(categories_items_amount,categories),
        "items":items,
    })


def contact(request:HttpRequest):
    return render(request, "core/contact.html",status=200)


def signup(request:HttpRequest):
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()

            if request.GET["next"]:
                return redirect(f"/login/?next={request.GET['next']}")
            else:
                return redirect("/login/")
    else:
        form = SignUpForm()

    return render(request, "core/signup.html", {
        "form":form
    })