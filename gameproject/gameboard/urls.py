from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('gamedetail/<str:game_id>', gamedetail, name ="gamedetail"),
    path('gamenew/', gamenew, name = "gamenew"),
    path('gameedit/<str:game_id>', gameedit, name = "gameedit"),
    path('gamedelete/<str:game_id>', gamedelete, name = "gamedelete"),
    path('gamesearch/', gamesearch, name='gamesearch'),
]