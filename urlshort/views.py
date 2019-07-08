from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from .models import UrlModel
import string, random
from django.template import RequestContext
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse

def generate_token():
    token = ''.join(random.choice(string.ascii_lowercase + string.digits + string.ascii_uppercase) for x in range(5))
    return token

def index(request):
    short_url = None
    token = generate_token()

    if request.method == "POST":
        link = UrlModel()
        link.url = request.POST.get('url')
        link.token = token
        link.save()

        short_url = request.build_absolute_uri(link.token)
    return render(request, 'urlshort/index.html', {'short_url': short_url, 'token': token})

def link_url(request, token):
    print("Redirecting url..................")
    link = get_object_or_404(UrlModel, token=token)
    print(link)
    return HttpResponseRedirect(link.url)









