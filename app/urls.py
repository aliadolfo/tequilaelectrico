from django.urls import path
from app.views import HomePageView, AboutPageView

app_name = 'app'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    ]
