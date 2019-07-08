from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name="uurl"
urlpatterns = [
    path('', views.index, name='home'),
    # path('<str:token>', views.redirect_url, name="short_url")
    path('<str:token>', views.link_url, name="short_url")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)