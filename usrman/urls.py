from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'ccp.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),
	url(r'^login/$', 'usrman.views.lin', name='login'),
	url(r'^logout/$', 'usrman.views.lout', name='logout'),
	url(r'^new/$', 'usrman.views.new', name='new'),
	url(r'^confirm/$', 'usrman.views.confirm', name='confirm'),
	url(r'^test/$', 'usrman.views.example', name='test'),
)