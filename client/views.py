from django.shortcuts import render
from .forms import ClientForm

def index(request):
   if request.method == 'GET':
      form = ClientForm()
      return render(request, 'client/index.html', {'form': form})

