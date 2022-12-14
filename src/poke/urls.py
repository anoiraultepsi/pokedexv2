from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('pokemon/<int:number>/',views.pokemon,name="pokemon"),
    path('search/<str:searchText>/',views.search,name="search"),
    path('about/',views.about,name="about"),
    path('team/<int:number>',views.team,name="team"),
    path('team/delall',views.delallteam,name="delallteam"),
    path('team/<int:number>/add',views.teamadd,name="teamadd"),
    path('team/<int:number>/del',views.teamdel,name="teamdel"),
]