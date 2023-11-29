from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h2>Главная</h2>")

def user(request, full_name, age, interests):
    return HttpResponse(f'''
            <h2>О пользователе</h2>
            <p>ФИО: {full_name}</p>
            <p>Возраст: {age}</p>
            <p>Интересы: {interests}</p>
''')

def about(request, is_from, performance, who_studies):
    return HttpResponse(f'''
            <h2>О пользователе</h2>
            <p>Я приехал из {is_from}</p>
            <p>У меня {performance} успеваемость в школе</p>
            <p>Я {who_studies} учиться</p>
''')

def contacts(request, github, vk):
    return HttpResponse(f'''
            <h2 style="font-family: Arial;">Контакты:</h2>
            <a href="{github}" style="font-size: 24px; font-family: Arial;">GitHub</a><br><br>
            <a href="{vk}" style="font-size: 24px; font-family: Arial;">ВК</a>
''')


