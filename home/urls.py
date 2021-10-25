from django.urls import path
from home.views import HomeView, downloadImage, register, add_rating
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', HomeView.as_view(), name='home-page'),
    path('signup/', register, name='sign-up-page'),
    path('getpic/', downloadImage, name='get-pic'),
    path('rating', add_rating,name='rating-create-page')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
