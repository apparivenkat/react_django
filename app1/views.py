from django.shortcuts import render
from .models import Contact

# Create your views here.

def create_contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        con = Contact.objects.create(name=name, email=email, phone=phone, address=address)
    obj = Contact.objects.all()
    return render(request, 'home.html', {'obj':obj})