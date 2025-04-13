from django.shortcuts import render, HttpResponse
import csv
import os
from .webscraper import run
from .webscraper2 import run2

def index(request):
    run() 
    run2()
    file_path = os.path.join(os.path.dirname(__file__), 'hackathon.csv')
    print(f"File path: {file_path}")
    data = []

    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader) 
        for row in reader:
            data.append(row)  

    return render(request, 'webscraper.html', {'hackathons': data})

def download_csv(request):
    
    file_path = os.path.join(os.path.dirname(__file__), 'hackathon.csv')

    
    response = HttpResponse(open(file_path, 'rb'), content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="hackathon.csv"'

    return response
