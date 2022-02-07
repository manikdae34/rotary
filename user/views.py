from urllib import request
from django.shortcuts import render
from django.views.generic import View

from django.contrib.auth.forms import UserCreationForm

# Create your views here.

class CreateUserView(View):
    def get(self, request):
        form = UserCreationForm()
        context = {
        'form': form
        }
        return render(request, 'user/create.html', context)



def index(request):
    return render(request, 'user/profile.html')