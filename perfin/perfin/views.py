from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Choice, Question


class HomeView(generic.ListView):
    model = Question
    template_name = 'perfin/home.html'

    def get_net_worth(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class BudgetView(generic.ListView):
    model = Question
    template_name = 'perfin/budget.html'


class InvestmentsView(generic.ListView):
    model = Question
    template_name = 'perfin/investments.html'


class NetWorthView(generic.ListView):
    model = Question
    template_name = 'perfin/networth.html'


class SettingsView(generic.ListView):
    model = Question
    template_name = 'perfin/settings.html'

