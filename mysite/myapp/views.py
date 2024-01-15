from django.shortcuts import render
from django.http import HttpResponse

import csv
import os
from io import TextIOWrapper
from .models import League, Year, Team, Participation, Person, Song, Parent
from django.shortcuts import render
from .models import Parent


def home(request):
    filtered_data = None

    if request.method == "POST":
        select_option = request.POST.get('selectOption')
        text_box_value = request.POST.get('textBox')

        if text_box_value:
            try:
                if select_option == 'league':
                    filtered_data = Parent.objects.filter(
                        league__number=int(text_box_value))
                elif select_option == 'year':
                    filtered_data = Parent.objects.filter(
                        year__number=int(text_box_value))
                elif select_option == 'team':
                    filtered_data = Parent.objects.filter(
                        team__string=str(text_box_value))
                elif select_option == 'participation':
                    filtered_data = Parent.objects.filter(
                        participation__number=str(text_box_value))
                elif select_option == 'person':
                    filtered_data = Parent.objects.filter(
                        person__string=str(text_box_value))
                elif select_option == 'song':
                    filtered_data = Parent.objects.filter(
                        song__string=str(text_box_value))
                else:
                    # 未知の選択肢に対する処理
                    pass
            except ValueError:
                # textBox の値が整数に変換できない場合のエラーハンドリング
                pass

    context = {'data': filtered_data}
    return render(request, 'home.html', context)


# ----- 名簿登録 -----
def upload(request):
    if 'csv' in request.FILES:
        form_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
        csv_file = csv.reader(form_data)

        for line in csv_file:
            league, _ = League.objects.get_or_create(number=line[0])  # 大会
            year, _ = Year.objects.get_or_create(number=line[1])  # 年
            team, _ = Team.objects.get_or_create(string=line[2])  # 組
            participation, _ = Participation.objects.get_or_create(
                number=line[3])  # 回数
            person, _ = Person.objects.get_or_create(string=line[4])  # 人
            song, _ = Song.objects.get_or_create(string=line[5])  # 曲名

            # Person以外のデータをもとにParentレコードを更新または新規作成
            # 既存のParentレコードを取得する
            existing_parent = Parent.objects.filter(
                league=league,
                year=year,
                team=team,
                participation=participation,
                song=song
            ).first()

            # 既存のParentレコードが存在する場合
            if existing_parent:
                # すでにPersonが追加されていない場合に追加
                parent.person.add(person)
            else:
                # Parentレコードが存在しない場合は新規作成
                parent = Parent.objects.create(
                    league=league,
                    year=year,
                    team=team,
                    participation=participation,
                    song=song,
                )
                parent.person.set([person])

    return render(request, 'upload.html')
