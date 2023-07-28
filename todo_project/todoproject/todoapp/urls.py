from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from todoapp import views
#app_name='todoapp'

#from django.contrib import admin
# for name space


urlpatterns = [
    path('',views.add ,name='add'),
    path('delete_task/<int:taskid>/', views.delete_task, name='delete_task'),
    path('update/<int:id>/',views.update,name='update'),
    path('TaskListView/',views.TaskListView.as_view(),name='TaskListView'),
    path('cbvdetail/<int:pk>/',views.TaskDetailView.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>/', views.TaskUpdateView.as_view(), name='cbvupdate'),
path('cbvdelete/<int:pk>/', views.TaskDeleteView.as_view(), name='cbvdelete'),


    #path('contact/',views.contact,name='contact')
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
