from django import forms

from .models import ConversationMessages


class ConverstionMessagesForm(forms.ModelForm):
    class Meta:
        model = ConversationMessages
        fields = ("content",)
    content = forms.CharField(max_length=2000, widget=forms.Textarea({"maxlength":"2000"}))