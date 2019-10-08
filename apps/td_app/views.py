from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from time import gmtime, strftime, localtime, time
from pytz import timezone
import pytz

# Create your views here.
def index(request):
    dt_mtn = datetime.now(tz=pytz.timezone('US/Mountain'))
    context = {
        "time": dt_mtn.strftime("%b %d, %Y %I:%M %p")
    }
    return render(request, "td_app/index.html", context)

def refresh(request):
    return redirect('/')



  





