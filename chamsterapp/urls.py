from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('nft', views.nftGallery, name="nftGallery"),
    path('nft/<str:pk>', views.nftProfile, name="nftProfile"),
]
