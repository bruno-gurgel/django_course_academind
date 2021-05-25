from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.


def monthly_challenge(request, month):
    challenge_text = None
    if month == 'january':
        challenge_text = "Eat no meat!"
    elif month == "february":
        challenge_text = "Walk for 20 minutes!"
    elif month == "march":
        challenge_text = "Learn Django for at least 20 minutes a day"
    else:
        return HttpResponseNotFound('This month is not supported!')
    return HttpResponse(challenge_text)
