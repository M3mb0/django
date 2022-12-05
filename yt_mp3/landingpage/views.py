from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.sessions.models import Session
import sys
import platform


# Create your views here.

class HomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        sessions = Session.objects.all()
        return {
            "py_version": sys.version,
            "os": platform.uname(),
            "sessions": sessions
        }
