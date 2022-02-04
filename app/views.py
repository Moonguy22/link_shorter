from operator import ge
from django.shortcuts import render, redirect
from .serializers import UrlSerializer, UrlCreateSerializer
from .models import Url
from rest_framework import generics
from django.shortcuts import get_object_or_404
from .forms import UrlForm
from django.conf import settings


class UrlListView(generics.ListAPIView):
    queryset = Url.objects.all()
    serializer_class = UrlSerializer


class UrlCreateView(generics.CreateAPIView):
    queryset = Url.objects.all()
    serializer_class = UrlCreateSerializer
    

def redirect_view(request, code):
    url = get_object_or_404(Url, short_code = code)
    return redirect(url.origin_url)


def detail(request):
    search = request.GET.get('q')
    form = UrlForm(request.POST or None)
    urls = Url.objects.all()
    if search:
        urls = urls.filter(origin_url__icontains=search)
    if request.method == "POST" and form.is_valid():
        form.save()

    return render(request, 'index.html', {'form': form, 'urls': urls, 'site_url': settings.SITE_URL })
    