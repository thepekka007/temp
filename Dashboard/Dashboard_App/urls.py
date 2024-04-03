from django.urls import path,re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    
    path('users/', views.users, name='users'),

     path('dashboard2', views.dashboard2, name='dashboard2'),
     path('form', views.form, name='form'),
      path('editform', views.editform, name='editform'),
      path('mydata', views.mydata, name='mydata'),
    
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)