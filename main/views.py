from django.shortcuts import render, redirect
from .models import Banner, About, Pricing, Room, Booking, Service, Our_services, Info, Contact, Gallery
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index_view(request):
    banners = Banner.objects.all()
    about_info = About.objects.all()
    pricings = Pricing.objects.all()
    our_services = Our_services.objects.all()
    info = Info.objects.last()
    contacts = Contact.objects.all()
    context = {
        'banners': banners,
        'about_info': about_info,
        'pricings': pricings,
        'our_services': our_services,
        'info': info,
        'contacts': contacts,
    }
    return render(request, 'index.html', context)


def room_view(request):
    rooms = Pricing.objects.all().order_by('-id')
    context = {
        'rooms': Pricing.objects.all(),
        'info': Info.objects.last()
    }
    return render(request, 'rooms.html', context)


def about_view(request):
    context = {
        'about': About.objects.all(),
        'services': Service.objects.all(),
        'l_gallery': Gallery.objects.all().order_by('-id')[:4],
        'info': Info.objects.last()
    }
    return render(request, 'about-us.html', context)


def contect_view(request):
    context = {
        'info': Info.objects.last()
    }
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        message = request.POST['message']
        contact = Contact.objects.create(
            full_name=full_name,
            email=email,
            message=message,
        )

        return redirect("contact_url")
    return render(request, 'contact.html', context)


