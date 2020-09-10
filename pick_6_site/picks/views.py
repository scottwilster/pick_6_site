from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse
from django.http import Http404
from .models import Pick


# Create your views here.
def index(request):
    latest_pick_list = Pick.objects.order_by('-pub_date')[:5]
    context = {'latest_pick_list': latest_pick_list}
    return render(request, 'picks/index.html', context)

# def results(request):
    # drop down menu to select all or individual user
    # date range selection
    # teams chosen, bet type, win/loss result with totals and %'s

# def selections
    # drop down menu to select user
    # user input pick_text (team name), bet type, pts, week number selected


