from django import forms
from .models import Items, FeedBacks


class NewItemForm(forms.ModelForm):

    class Meta:
        model = Items
        fields = ("name", "description", "price", "image", "category")
        
        widgets = {
            "name":forms.TextInput({"placeholder": "Name of product"}),
            "description":forms.Textarea({"placeholder": "Description"}),
            "price":forms.TextInput({"placeholder": "Price"}),
            "image":forms.FileInput(),
            "category":forms.Select()
        }



class EditItemForm(forms.ModelForm):

    class Meta:
        model = Items
        fields = ("name", "description", "price", "image", "sold")
        
        widgets = {
            "name":forms.TextInput({"placeholder": "Name of product"}),
            "description":forms.Textarea({"placeholder": "Description"}),
            "price":forms.TextInput({"placeholder": "Price"}),
            "image":forms.FileInput()
        }


class AddFeedBackForm(forms.ModelForm):

    class Meta:
        model = FeedBacks
        fields = ("rating", "content")
    
    content = forms.CharField(max_length=2000, widget=forms.Textarea({"placeholder":"Feedback"}))
    rating = forms.IntegerField(max_value=5, min_value=0, widget=forms.HiddenInput())