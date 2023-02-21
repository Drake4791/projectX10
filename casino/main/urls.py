from django.urls import path
from . import views
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import logout_then_login
urlpatterns = [
    path('', views.index, name='rise'),
    path('ref', views.ref, name='referal'),
    path('token_investing', views.token_investing, name='token_investing'),
    path('nft_collection', views.nft_collection, name='nft_collection'),
    path('airdrop', views.airdrop, name='airdrop'),
]