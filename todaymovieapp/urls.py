from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from todaymovieapp.views import main, TodaymovieCreateView, TodaymovieDetailView, TodaymovieUpdateView, TodaymovieDeleteView

app_name = "todaymovieapp"

urlpatterns = [
    path('main/', main, name='main'),

    path('login/', LoginView.as_view(template_name='todaymovieapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('create/', TodaymovieCreateView.as_view(), name='create'),
    path('detail/<int:pk>', TodaymovieDetailView.as_view(), name='detail'),
    path('update/<int:pk>', TodaymovieUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', TodaymovieDeleteView.as_view(), name='delete'),
]