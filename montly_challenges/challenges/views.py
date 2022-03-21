from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

monthly_challenges ={
    "january":"Eat no meat for the entire month",
    "february":"Walk for at least 20 minutes every day",
    "march":"Learn Django for at least 20 minutes every day",
    "april":"Eat no meat for the entire month",
    "may":"Walk for at least 20 minutes every day",
    "june":"Eat no meat for the entire month",
    "july":"Learn Django for at least 20 minutes every day",
    "august":"Walk for at least 20 minutes every day",
    "september":"Eat no meat for the entire month",
    "octomber":"Learn Django for at least 20 minutes every day",
    "november":"Walk for at least 20 minutes every day",
    "december":"Eat no meat for the entire month"
}


# Create your views here.

def index(response):
    list_items = ""
    months = list(monthly_challenges.keys())
    
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month]) 
        list_items += f"<li> <a href=\"{month_path}\">{capitalized_month}</li>"

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

def monthly_challenge_by_number(request,month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge",args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request,month):

    try:
        challenge_txt = monthly_challenges[month]
        response_data = f"<h1>{challenge_txt}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("This month are not available, SORRY!")

# def january(request):
#     return HttpResponse("No meat entire full month")

# def february(request):
#     return HttpResponse("Wolk for at least 20 miutes every day")

# def monthly_challenge(request,month):
    # challenge_txt = None
    # if month == "january":
    #     challenge_txt = "Eat no meat the entire month"
    # elif month == "february":
    #     challenge_txt = "Walk for at least 20 minutes every day!"
    # elif month == "march":
    #     challenge_txt = "Learn Django for at least 20 minutes every day"
    # else:
    #     return HttpResponseNotFound("this month are not available")
    # return HttpResponse(challenge_txt)