# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.views.generic.base import View


TEAMS = {
    'Sénégal': ['Marlyatou Diallo', 'Issa Diallo'],
    'Tunisie': ['Inès Mildani'],
}


class TeamsView(View):
    def get(self, request):
        return render(request, 'home.html', {'object_list': TEAMS.items()})
