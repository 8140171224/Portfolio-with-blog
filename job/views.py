from django.shortcuts import render
from .models import Job
# Create your views here.
def home(request):
    job = Job.objects
    return render(request, 'job/home.html', {'job':job})
