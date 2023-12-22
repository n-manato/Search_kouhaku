from django.shortcuts import render
from django.http import HttpResponse

import csv
import os
from io import TextIOWrapper
from .models import League, Year, Team, Participation, Person, Song, Parent

# Create your views here.


def home(request):
    return HttpResponse("Hello world!")


# ----- 名簿登録 -----
def upload(request):
    if 'csv' in request.FILES:
        form_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
        csv_file = csv.reader(form_data)

        for line in csv_file:
            League.objects.get_or_create(number=line[0])  # 大会
            Year.objects.get_or_create(number=line[1])  # 年
            Team.objects.get_or_create(string=line[2])  # 組
            Participation.objects.get_or_create(number=line[3])  # 回数
            Person.objects.get_or_create(string=line[4])  # 人
            Song.objects.get_or_create(string=line[5])  # 曲名

    return render(request, 'upload.html')
