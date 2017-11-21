from django.conf.urls import url
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^registeration$',views.get_form,name='get_form' ),
    url(r'^log_in',views.log_in,name='log_in' ),
    url(r'^welcome.html$',views.welcome ),
    url(r'^admin/', admin.site.urls),
]