from django.shortcuts import render, redirect
from .models import QR
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

@login_required
def home(request):
    context = {
        "Qr": QR.objects.all().first()
    }
    return render(request, "index.html", context=context)

def cierre(request):
    logout(request)
    return redirect('/')