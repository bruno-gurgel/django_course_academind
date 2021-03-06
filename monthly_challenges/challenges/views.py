from django.shortcuts import render
from django.http import (Http404, HttpResponseNotFound,
                         HttpResponseRedirect)
from django.urls.base import reverse

# Create your views here.


def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })


monthly_challenges = {
    'january': 'Eat no meat!',
    'february': 'Walk for 20 minutes!',
    'march': 'Learn Django for at least 20 minutes a day',
    'april': 'Eat no meat!',
    'may': 'Eat no meat!',
    'june': 'Walk for 20 minutes!',
    'july': 'Eat no meat!',
    'august': 'Learn Django for at least 20 minutes a day',
    'september': 'Walk for 20 minutes!',
    'october': 'Eat no meat!',
    'november': 'Learn Django for at least 20 minutes a day',
    'december': None,
}


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound('Invalid month!')

    redirect_month = months[month - 1]
    redirect_path = reverse('month-challenge', args=[redirect_month])

    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html",  {
            "text": challenge_text,
            "month_name": month
        })
    except:
        raise Http404()
