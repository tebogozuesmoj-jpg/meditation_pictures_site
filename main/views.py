from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from .models import ContactMessage


def home(request):
    return render(request, 'main/home.html')

# Commented out book view as per your current state
# def book(request):
#     return render(request, 'main/book.html')

def services(request):
    services_list = [
        {"title": "Family Photoshoots", "description": "Capture beautiful moments with your loved ones."},
        {"title": "Wedding Photography", "description": "Professional photography for your wedding day."},
        {"title": "Corporate Events", "description": "Event coverage for corporate needs."},
        {"title": "Videography", "description": "High quality video productions."},
        {"title": "Photo Editing Services", "description": "Professional photo retouching and editing."},
    ]
    return render(request, 'main/services.html', {'services': services_list})

def portfolio(request):
    categories = [
        {
            "title": "Weddings",
            "image": "portfolio1.jpg",
            "instagram_url": "https://instagram.com/meditation.pictures_za",
        },
        {
            "title": "Schools",
            "image": "portfolio2.jpg",
            "instagram_url": "https://instagram.com/meditation.pictures_za",
        },
        {
            "title": "Studio",
            "image": "studio.jpg",
            "instagram_url": "https://instagram.com/meditation.pictures_za",
        },
        {
            "title": "Corporate",
            "image": "corporate.jpg",
            "instagram_url": "https://instagram.com/meditation.pictures_za",
        },
        {
            "title": "Lifestyle",
            "image": "lifestyle.jpg",
            "instagram_url": "https://instagram.com/meditation.pictures_za",
        },
    ]
    return render(request, "main/portfolio.html", {"categories": categories})


def about(request):
    context = {
        "company_story": "Meditation Pictures is dedicated to capturing your most authentic moments with passion and professionalism.",
        "team_members": [
            {"name": "Alice Johnson", "role": "Lead Photographer", "bio": "With over 10 years of experience, Alice specializes in family and wedding photography."},
            {"name": "Bob Smith", "role": "Videographer", "bio": "Bob creates stunning videos that bring your stories to life."},
        ],
        "testimonials": [
            {"client": "Samantha Lee", "comment": "Absolutely loved the photos! The team was professional and made us feel at ease."},
            {"client": "Michael Rodriguez", "comment": "High-quality service and amazing attention to detail."},
        ],
    }
    return render(request, 'main/about.html', context)


def contact(request):
    success = False
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save to DB
            ContactMessage.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['message']
            )
            # Prepare email
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            full_message = f"Message from {name} <{email}>:\n\n{message}"

            send_mail(
                subject=f"New Contact Form Submission: {subject}",
                message=full_message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=['zuespink@gmail.com'],  # Replace with actual client email
                fail_silently=False,
            )
            success = True
            form = ContactForm()  # Reset form after successful send
    else:
        form = ContactForm()

    return render(request, "main/contact.html", {
        "form": form,
        "page_title": "Contact Us",
        "success": success,
    })
