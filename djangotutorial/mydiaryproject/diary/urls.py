from django.urls import path
from . import views

app_name = 'diary'
urlpatterns = [
  # 第1引数：アクセスされる URL の定義
  # 
  path('index/', views.IndexView.as_view(), name='index'),
]