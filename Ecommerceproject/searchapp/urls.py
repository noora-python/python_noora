from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .import  views
app_name='searchapp'

#from django.contrib import admin
# for name space


urlpatterns = [
    path('',views.SearchApp ,name='SearchApp'),



    #path('contact/',views.contact,name='contact')
]
