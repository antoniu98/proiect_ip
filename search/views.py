from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage

from .forms import AdForm
from .models import Advertisment
from .filters import AdvertismentFilter

def search(response):
    ads = Advertisment.objects.all()
    ads_count = ads.count()

    ads_filter = AdvertismentFilter(response.GET, queryset = ads)
    orders = ads_filter.qs

    return render(response, "search.html", {'Ads': orders, 'filter' : ads_filter})

def upload_ad(response):
    if response.method == 'POST':
        form = AdForm(response.POST, response.FILES)
        if form.is_valid():
            form.save()
            return redirect('search')
    else:
        form = AdForm()
    return render(response, 'upload_ad.html', {
        'form': form
    })

def update_ad(response, pk):
    ad = Advertisment.objects.get(pk=pk)
    form = AdForm(instance=ad)
    if response.method == 'POST':
        form = AdForm(response.POST, instance=ad)
        if form.is_valid():
            form.save()
            return redirect('search')

    return render(response, 'upload_ad.html', {
        'form': form
    })

def delete_ad(response, pk):
    if response.method == 'POST':
        ad = Advertisment.objects.get(pk = pk)
        ad.delete()
    return redirect('search')
