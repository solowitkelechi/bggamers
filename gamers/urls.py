from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('adminpanel/', views.adminpanel, name='adminpanel'),
    path('addplayer/', views.addplayer, name='addplayer'),
    path('addwinners/', views.addwinners, name='addwinners'),
    path('addgame/', views.addgame, name='addgame'),
    path('togglestatus/', views.togglestatus, name='togglestatus'),
    path('playerstogame/', views.playerstogame, name='playerstogame'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

