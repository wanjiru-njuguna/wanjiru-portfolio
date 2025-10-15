from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["name", "email", "website", "comment"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Name*", "required": True}),
            "email": forms.EmailInput(attrs={"placeholder": "Email*", "required": True}),
            "website": forms.URLInput(attrs={"placeholder": "Website"}),
            "comment": forms.Textarea(attrs={"placeholder": "Type here..", "rows": 5}),
        }
        labels = {
            "name": "Name*",
            "email": "Email*",
            "website": "Website",
            "comment": "Comment",
        }