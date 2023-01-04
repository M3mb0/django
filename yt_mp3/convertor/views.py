from django.shortcuts import render
from django.views import View
from .utils import mp3_download
from .models import Conversion
from django.core.files import File
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


# Create your views here.


class SearchView(LoginRequiredMixin, View):

    def get(self, req):
        context = {
            "zoom": req.GET.get("zoom", "1")
        }

        return render(req, "search.html", context)

    def post(self, req):
        out_file, file_name = mp3_download(req.POST.get('url'))
        out_file.seek(0)  # reset the buffer reader head
        downloaded_file = File(out_file, name=file_name)
        conversion = Conversion(
            yt_url=req.POST.get('url'),
            user=req.user,
            file=downloaded_file
        )
        conversion.save()
        return render(req, "download_ready.html", {"conv": conversion})


class HistoryView(LoginRequiredMixin, TemplateView):
    template_name = "history.html"

    def get_context_data(self, **kwargs):
        output_history = Conversion.objects.filter(user=self.request.user)
        return {"output_history": output_history}