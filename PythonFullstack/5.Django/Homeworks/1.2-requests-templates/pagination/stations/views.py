from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv

from pagination.pagination.settings import BUS_STATION_CSV

def index(request):
    return redirect(reverse('bus_stations'))

print(BUS_STATION_CSV)
CONTENT = csv.DictReader(BUS_STATION_CSV)


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(CONTENT, 10)
    page = paginator.get_page(page_number)
    bus_stations = []
    with open(BUS_STATION_CSV, newline='') as csvfile:
        for row in CONTENT:
            bus_stations.append(row)
    context = {
        'bus_stations': bus_stations,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
