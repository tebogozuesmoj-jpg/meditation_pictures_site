from django import forms

TAILWIND_INPUT_CLASSES = (
    "border border-gray-300 rounded-md p-2 w-full focus:outline-none focus:ring-2 focus:ring-blue-500"
)

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label="Name",
        widget=forms.TextInput(attrs={"class": TAILWIND_INPUT_CLASSES}),
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={"class": TAILWIND_INPUT_CLASSES}),
    )
    subject = forms.CharField(
        max_length=150,
        label="Subject",
        widget=forms.TextInput(attrs={"class": TAILWIND_INPUT_CLASSES}),
    )
    message = forms.CharField(
        label="Message",
        widget=forms.Textarea(attrs={"class": TAILWIND_INPUT_CLASSES, "rows": 5}),
    )
