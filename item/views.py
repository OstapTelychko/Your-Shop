from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.conf import settings
from django.urls import reverse

import os
from .forms import NewItemForm, EditItemForm, AddFeedBackForm
from .models import Items, Categories, FeedBacks




def search(request:HttpRequest):
    query = request.GET.get("query","")
    category_id = request.GET.get("category", 0)
    items = Items.objects.filter(sold=False)
    categories = Categories.objects.all()

    if category_id:
        items = items.filter(category=category_id)
        
    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, "item/search.html", {
        'items': items, 
        "query":query,
        "categories":categories,
        "category_id":int(category_id)
        })



def details(request:HttpRequest, id:int):
    item = get_object_or_404(Items, id=id)

    if request.method == "POST":#User sent feedback

        if request.user.is_authenticated:
            form = AddFeedBackForm(request.POST)

            if int(form["rating"].value()) in (1, 2, 3, 4, 5):#If somebody changed input value
                if form.is_valid():
                    print(form["rating"].value() == "")
                    feedback = form.save(commit=False)
                    feedback.owner = request.user
                    feedback.item = item
                    feedback.save()

                    return redirect("item:details", id=item.id)
        else:
            path_back_to_item = reverse("item:details", args=(item.id,))
            path = f"{reverse('core:signup')}?next={path_back_to_item}"
            return redirect(path)
        
    else:

        feedbacks = FeedBacks.objects.filter(item = item)
        form = AddFeedBackForm(initial={"rating":1})

        if request.user == item.owner:
            related_items = Items.objects.filter(category=item.category, sold = False).exclude(id=id)[:3]

            return render(request, "item/details.html",{
                "item":item,
                "related_items":related_items,
                "feedbacks":feedbacks
            })
        else:
            if not item.sold:
            # item_for_user = get_object_or_404(Items, id=id, sold=False)
                related_items = Items.objects.filter(category=item.category, sold = False).exclude(id=id)[:3]
                
                return render(request, "item/details.html",{
                    "item":item,
                    "related_items":related_items,
                    "feedbacks":feedbacks,
                    "form":form
                })


@login_required
def add(request:HttpRequest):
    if request.method == "POST":
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.owner = request.user
            item.save()

            return redirect("item:details", id=item.id)
    else:
        form = NewItemForm()

    return render(request, "item/add|edit.html", {
        "form":form,
        "title": "New Item",
    })


@login_required
def edit(request:HttpRequest, id:int):
    item = get_object_or_404(Items, id=id, owner=request.user)

    if request.method == "POST":
        form = EditItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()

            return redirect("item:details", id=item.id)
    else:
        form = EditItemForm(instance=item)

    return render(request, "item/add|edit.html", {
        "form":form,
        "title": "Edit Item",
    })


@login_required
def remove(request:HttpRequest, id:int):
    item = get_object_or_404(Items, id=id, owner=request.user)
    if item.image:
        os.remove(f"{settings.MEDIA_ROOT}/{item.image}")
    item.delete()

    return redirect("dashboard:user home")
