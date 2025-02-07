from django.urls import path
from django.http import HttpResponse

def home(request):
    return HttpResponse("Привет, это главная страница!")

urlpatterns = [
    path('', home, name='home'),  # Добавляем путь на главную
]

