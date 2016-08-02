from django.conf.urls import url
import views as home_views

urlpatterns =[
    url(r'^new/player', home_views.new_player),
    url(r'^player/(?P<id>\d+)/$', home_views.player_details, name='playerdetails'),
        ]