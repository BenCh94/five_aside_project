from django.conf.urls import url
import views as blog_views

urlpatterns =[
    url(r'^blog/$', blog_views.post_list, name='blogview'),
    url(r'^blog/(?P<id>\d+)/$', blog_views.post_details, name='blogdetails'),
    url(r'^post/new$', blog_views.new_post, name="new_post"),
    url(r'^blog/(?P<id>\d+)/edit$', blog_views.edit_post, name="edit"),
    url(r'^popular/$', blog_views.post_list_by_views, name="popular"),

        ]