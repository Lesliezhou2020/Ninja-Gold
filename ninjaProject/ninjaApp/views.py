from django.shortcuts import render, redirect
from time import gmtime, strftime
import random

def index(request):
    if 'amount' not in request.session:
        request.session['amount'] = 0
    
    if 'activities' not in request.session:
        request.session['activities'] = []

    return render(request, "index.html")


def process_money(request):
    if request.method == 'POST':

        dt = strftime("%Y/%m/%d %I:%M %p", gmtime())

        if request.POST['location'] == '1001':
            earning = random.randint(10, 20)
            activity = f'Earned {earning} golds from the farm! ({dt})'
        elif request.POST['location'] == '1002':
            earning = random.randint(5, 10)
            activity = f'Earned {earning} golds from the cave! ({dt})'
        elif request.POST['location'] == '1003':
            earning = random.randint(2, 5)
            activity = f'Earned {earning} golds from the house! ({dt})'
        else:
            earning = random.randint(-50, 50)
            if earning < 0:
                activity = f'Entered a casino and lost {-earning} golds... Ouch.. ({dt})'
            else:
                activity = f'Entered a casino and earn {earning} golds... Yeah.. ({dt})'
           

        request.session['amount'] += earning
        request.session['activities'].append(activity)

    return redirect("/")

def reset(request):
    request.session['amount'] = 0
    request.session['activities'] = []

    return redirect("/")
    