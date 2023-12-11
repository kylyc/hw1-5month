from django.shortcuts import render
from .models import Settings, Portfolio, Work, Clients, Info
# Create your views here.

def index(request):
    settings_all = Settings.objects.all()
    settings = Settings.objects.latest('id')
    portfolio_all = Portfolio.objects.all()
    work_all = Work.objects.all()
    clients_all = Clients.objects.all()
    info = Info.objects.latest('id')
    return render(request,"index.html", locals())   