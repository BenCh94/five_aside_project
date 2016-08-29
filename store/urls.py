from django.conf.urls import url
import views as store_views


urlpatterns =[
    url(r"^store/$", store_views.storefront),
    url(r'^charge/$', store_views.charge, name='charge'),
    url(r'^charge/thanks/$', store_views.thanks, name='thanks'),
    url(r"^checkout/$", store_views.checkout, name='checkout')
    ]