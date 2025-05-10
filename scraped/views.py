from django.shortcuts import render, HttpResponse
import csv
import os
from .webscraper import run
from .webscraper2 import run2
import threading
from scraped.models import Contest
import time
listfunc=[run,run2]
def index(request):
    Contest.objects.all().delete()
    for i in listfunc:
        thread=threading.Thread(target=i)
        thread.start()
        thread.join()
    data = Contest.objects.all()   
    return render(request, 'webscraper.html', {'hackathons': data})

def download_csv(request):
    
    file_path = os.path.join(os.path.dirname(__file__), 'hackathon.csv')

    
    response = HttpResponse(open(file_path, 'rb'), content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="hackathon.csv"'

    return response
