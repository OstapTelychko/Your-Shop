from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpRequest

from item.models import Items


@login_required
def user_home(request:HttpRequest):
    items = Items.objects.filter(owner=request.user)

    return render(request, "dashboard/user home.html", {'items': items})


