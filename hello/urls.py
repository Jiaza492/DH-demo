from django.conf.urls import patterns, url
import hello.views
# define a action url for list post method
urlpatterns = [
               url(r'^$',hello.views.search, name="search"),
               ]