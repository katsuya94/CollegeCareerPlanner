from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'ccp.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),

	url(r'^admin/', include(admin.site.urls)),
	url(r'^plan/', include('plan.urls', namespace='plan')),
	url(r'^usrman/', include('usrman.urls', namespace='usrman')),
)
