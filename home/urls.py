from django.urls import path
from home.views import HomeView, downloadImage, register, addRating, RatingUpdateView, seeAllRatings
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', HomeView.as_view(), name='home-page'),
    path('signup/', register, name='sign-up-page'),
    path('getpic/', downloadImage, name='get-pic'),
    path('rating_add/', addRating,name='rating-create-page'),
    path('rating_update/<int:pk>', RatingUpdateView.as_view(), name='rating-update-page'),
    path('see_all_ratings', seeAllRatings, name='see-all-ratings-page')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
