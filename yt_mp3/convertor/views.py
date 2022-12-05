from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from .utils import mp3_download
from .models import Conversion


# Create your views here.

class SearchView(View):

    def get(self, req):
        if req.user.is_authenticated:
            template_name = "search.html"
        else:
            template_name = "not_allowed.html"
        return render(req, template_name)

    def post(self, req):
        out_file = mp3_download(req.POST.get('url'))
        Conversion.objects.create(
            yt_url=req.POST.get('url'),
            user=req.user
        )
        return render(req, "download_ready.html",   {"out_path":out_file})