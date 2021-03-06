from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'unified_test.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^', include('UnifiedTest.urls')),
                       url(r'^', include('user_management.urls')),
                       url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/login'}, name='logout'),
                       url('', include('django.contrib.auth.urls', namespace='auth')),
)
