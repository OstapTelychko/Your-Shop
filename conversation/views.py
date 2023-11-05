from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest

from item.models import Items
from .forms import ConverstionMessagesForm
from .models import Conversations



@login_required
def new_conversation(request:HttpRequest, item_id:int):
    item = get_object_or_404(Items, id=item_id)

    if item.owner == request.user:
        return redirect("dashboard:user home")

    conversation = Conversations.objects.filter(item=item).filter(members__in=[request.user.id])

    if conversation:
        return redirect("conversation:chat", id=conversation.first().id)

    if request.method == "POST":
        form = ConverstionMessagesForm(request.POST)

        if form.is_valid():
            conversation = Conversations.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.owner)
            conversation.save()

            conversation_massages = form.save(commit=False)
            conversation_massages.conversation = conversation
            conversation_massages.owner = request.user
            conversation_massages.save()

            return redirect("item:details", id=item_id)
    else:
        form = ConverstionMessagesForm()
    
    return render(request, "conversation/new.html", {"form":form})


@login_required
def inbox(request:HttpRequest):
    conversations = Conversations.objects.filter(members__in=[request.user.id])

    return render(request, "conversation/inbox.html", {"conversations":conversations})


@login_required
def chat(request:HttpRequest, id:int):
    conversation = get_object_or_404(Conversations, members__in=[request.user.id], id=id)

    if request.method == "POST":
        form = ConverstionMessagesForm(request.POST)

        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.owner = request.user
            conversation_message.save()
            conversation.save()

            return redirect("conversation:chat", id=id)
    else:
        form = ConverstionMessagesForm()
        
    return render(request, "conversation/chat.html", {
        "conversation":conversation,
        "form":form
        })


