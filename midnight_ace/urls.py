"""
URL configuration for midnight_ace project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from midnight_ace import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
  path('admin/', admin.site.urls),
  path('midnight_ace/', views.card_list),
  path('midnight_ace/<str:suit>/', views.card_detail),
  path('midnight_ace/<int:score>/', views.player_detail),
  path('midnight_ace/<str:players>/', views.game_detail),
  path('midnight_ace/<int:number>/', views.round_detail),
  path('midnight_ace/<int:amount>/', views.bet_detail),
  path('midnight_ace/str:card>/', views.deck_detail)

]

urlpatterns = format_suffix_patterns(urlpatterns)
