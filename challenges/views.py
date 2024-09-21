from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def january(request):
    return HttpResponse("Eat no meats!")

def february(request):
    return HttpResponse("Walk for at least 20 minutes every day!")

def monthly_challenges(request, month): # django will pass the request name set in url configs (<month>) to the second argument of the veiw function (month) * arg names must match (month)
    challenge_text = None
    if month == "january":
        challenge_text = "Eat no meats!"
    elif month == "february":
        challenge_text = "Walk for at least 20 minutes every day!"
    elif month == "march":
        challenge_text = "Swim!"
    else:
        return HttpResponseNotFound("This month is not supported...")
    return HttpResponse(challenge_text)