from django.urls import path
from convertor.views import SearchView, HistoryView

app_name = 'convertor'
urlpatterns = [
    path('convertor', SearchView.as_view(), name='convertor'),
    path('history', HistoryView.as_view(), name='history'),
]