from django.urls import path
from django.views.generic import TemplateView

app_name = 'contentapp'

urlpatterns = [
    path('movie', TemplateView.as_view(template_name='contentapp/movie.html'), name='movie'),
    path('tvshow', TemplateView.as_view(template_name='contentapp/tvshow.html'), name='tvshow'),

    path('list/moaction', TemplateView.as_view(template_name='contentapp/movie/moaction.html'), name='moaction'),
    path('list/moadven', TemplateView.as_view(template_name='contentapp/movie/moadven.html'), name='moadven'),
    path('list/moani', TemplateView.as_view(template_name='contentapp/movie/moani.html'), name='moani'),
    path('list/mocomedy', TemplateView.as_view(template_name='contentapp/movie/mocomedy.html'), name='mocomedy'),
    path('list/mocrime', TemplateView.as_view(template_name='contentapp/movie/mocrime.html'), name='mocrime'),
    path('list/modocu', TemplateView.as_view(template_name='contentapp/movie/modocu.html'), name='modocu'),
    path('list/mofamily', TemplateView.as_view(template_name='contentapp/movie/mofamily.html'), name='mofamily'),
    path('list/mofanta', TemplateView.as_view(template_name='contentapp/movie/mofanta.html'), name='mofanta'),

    path('list/tvaction', TemplateView.as_view(template_name='contentapp/tvshow/tvaction.html'), name='tvaction'),
    path('list/tvadven', TemplateView.as_view(template_name='contentapp/tvshow/tvadven.html'), name='tvadven'),
    path('list/tvani', TemplateView.as_view(template_name='contentapp/tvshow/tvani.html'), name='tvani'),
    path('list/tvcomedy', TemplateView.as_view(template_name='contentapp/tvshow/tvcomedy.html'), name='tvcomedy'),
    path('list/tvcrime', TemplateView.as_view(template_name='contentapp/tvshow/tvcrime.html'), name='tvcrime'),
    path('list/tvdocu', TemplateView.as_view(template_name='contentapp/tvshow/tvdocu.html'), name='tvdocu'),
    path('list/tvfamily', TemplateView.as_view(template_name='contentapp/tvshow/tvfamily.html'), name='tvfamily'),
    path('list/tvfanta', TemplateView.as_view(template_name='contentapp/tvshow/tvfanta.html'), name='tvfanta'),

    path('creator', TemplateView.as_view(template_name='contentapp/creator.html'), name='creator'),

]