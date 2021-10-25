from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from home.forms import UserRegistrationForm
from django.contrib import messages

# Create your views here.

class HomeView(ListView):
    """ Renders a list of all Pages. """

    def get(self, request):
        """ GET a list of Pages. """
        return render(request, 'home/home.html')


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