from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .import  views
app_name='shop'

#from django.contrib import admin
# for name space


urlpatterns = [
    path('',views.allProdCaT ,name='allProdCaT'),
    path('<slug:c_slug>/',views.allProdCaT,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.ProDetail,name='prodCatDetails'),


    #path('contact/',views.contact,name='contact')
]
