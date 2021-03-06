from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic import UpdateView
from home.forms import RatingForm, UserRegistrationForm
from django.contrib import messages

from home.models import NasaImage, Rating
from django.core.files import File 
import requests
import uuid   
from django.contrib.auth.models import User

import urllib.request

class HomeView(ListView):
    def get(self, request):
        nasaPics = NasaImage.objects.all()
        nasaPic = nasaPics[len(nasaPics)-1]
        nasaRatings = Rating.objects.filter(nasaImage=nasaPic)
        nasaRating = None
        for rating in nasaRatings:
            print(rating.username, request.user.username)
            if rating.username == request.user:
                nasaRating = rating
                break
        return render(request, 'home/home.html', {'nasaImage': nasaPic, 'nasaRating': nasaRating})

def register(request):
    """To show a register form so a user can creat account"""
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'home/register.html', {'form': form})

def downloadImage(request):
    url = "https://api.nasa.gov/planetary/apod?api_key=uQ7H6lYnPUYvkesIXi8CDO1XhZEEAJO8Wr0Q6oHU"
    resp = requests.get(url)
    print(resp.json()['url'])
    httpUrl = resp.json()['url']
    result = urllib.request.urlretrieve(httpUrl)
    nasaPic = NasaImage()            
    nasaPic.image.save(str(uuid.uuid4())+".jpg", File(open(result[0], 'rb')))
    nasaPic.save()
    nasaPics = NasaImage.objects.all()
    nasaPic = nasaPics[len(nasaPics)-1]
    nasaRatings = Rating.objects.filter(nasaImage=nasaPic)
    nasaRating = None
    for rating in nasaRatings:
        if rating.username == request.user:
            nasaRating = rating
            break
    return render(request, 'home/home.html', {'nasaImage': nasaPic, 'nasaRating': nasaRating})

def addRating(request):
    nasaImages = NasaImage.objects.all()
    nasaImage = nasaImages[len(nasaImages)-1]

    form = RatingForm(request.POST)

    if request.method == "POST":
        if form.is_valid():
          rating = form.save(commit=False)
          rating.username = request.user
          rating.nasaImage = nasaImage
          rating.save()
          return redirect('/')
    else:
        form = RatingForm()
    return render(request, 'home/rating.html', {'form': form, 'nasaImage': nasaImage})

def seeAllRatings(request):
    nasaPics = NasaImage.objects.all()
    nasaPic = nasaPics[len(nasaPics)-1]
    nasaRatings = Rating.objects.filter(nasaImage=nasaPic)
    nasaRating = None
    return render(request, 'home/home.html', {'nasaImage': nasaPic, 'nasaRating': nasaRating, 'nasaRatings': nasaRatings})

class RatingUpdateView(UpdateView):
    model = Rating
    template_name = 'home/rating.html'
    form_class = RatingForm
    success_url = '/'


