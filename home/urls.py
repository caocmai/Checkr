from django.urls import path
from home.views import HomeView, register


urlpatterns = [
    path('', HomeView.as_view(), name='home-page'),
    path('signup/', register, name='sign-up-page')
]