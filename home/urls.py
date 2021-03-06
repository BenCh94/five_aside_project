from django.conf.urls import url
import views as home_views

urlpatterns =[
    url(r'^new/player', home_views.new_player),
    url(r'^player/(?P<id>\d+)/delete', home_views.delete_player, name='delete'),
    url(r'^player/(?P<id>\d+)/$', home_views.player_details, name='playerdetails'),
    url(r'^new_match/$', home_views.new_match, name='newmatch'),
    url(r'^create_teams/$', home_views.create_teams, name='create_teams'),
        ]