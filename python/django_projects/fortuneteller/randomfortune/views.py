import random
from django.shortcuts import render

# Create your views here.

fortuneList = ["You will succeed in life",
               "There is a challenge coming your way",
               "Sorry, we are out of fortunes today",
               ]


def fortune(request):
    fortune = random.choice(fortuneList)
    context = {"fortune": fortune}
    return render(request, "fortune.html", context)
