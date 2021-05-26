from django.shortcuts import render
from django.http import (HttpResponse, HttpResponseNotFound,
                         HttpResponseRedirect)
from django.urls.base import reverse

# Create your views here.


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse('month-challenge', args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    response_data = f"<ul>{list_items}</ul>"

    return HttpResponse(response_data)


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
    'december': 'Eat no meat!',
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
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound('This month is not supported!')
