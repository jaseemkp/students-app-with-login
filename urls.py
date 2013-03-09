from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()
from students.views import main_page, details, view, sort_age, sort_mark, remove_details, search, login_details, login_remove

urlpatterns = patterns('',('^$', main_page), (r'^admin/', include(admin.site.urls)),('^details/$', login_details),('^login_details/details/$',details),('^view/$',view),('^sort_age/$', sort_age),('^sort_mark/$', sort_mark),('^remove/$', login_remove),('^login_remove/remove/$',remove_details),('^search/$', search),)
