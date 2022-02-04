from django.urls import path
from .views import UrlListView , UrlCreateView, redirect_view, detail 

app_name='app'

urlpatterns = [
    path('list/', UrlListView.as_view()),
    path('create/', UrlCreateView.as_view()),
    path('<str:code>/', redirect_view),
    path('', detail, name='main' )
]

