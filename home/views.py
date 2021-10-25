from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from home.forms import UserRegistrationForm
from django.contrib import messages

from home.models import NasaImage
from django.core.files import File 
from io import BytesIO
import requests

from django.http import HttpResponse

import uuid   



import urllib.request


# Create your views here.

class HomeView(ListView):
    """ Renders a list of all Pages. """

    def get(self, request):
        """ GET a list of Pages. """
        nasaPics = NasaImage.objects.all()
        
        return render(request, 'home/home.html', {'nasaImage': nasaPics[len(nasaPics)-1]})


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
    # if resp.status_code != requests.codes.ok:
    #     #  Error handling here
    #     print("error")
    httpUrl = resp.json()['url']
    result = urllib.request.urlretrieve(httpUrl)
    nasaPic = NasaImage()            
    nasaPic.image.save(str(uuid.uuid4())+".jpg", File(open(result[0], 'rb')))
    nasaPic.save()
    nasaPics = NasaImage.objects.all()
    return render(request, 'home/home.html', {'nasaImage': nasaPics[len(nasaPics)-1]})
