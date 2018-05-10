from django.conf.urls import url

from . import views

urlpatterns = [
	
    url(r'^$', views.mom, name='mom'),
]
	#url(r'^search_form$',views.search_form,name='search_form'),
	#url(r'^Mothers_Day/search$',views.search,name='search'),
	# ex: /Mothers_Day/
	#url(r'^$',views.index,name='index'),
	# ex: /Mothers_Day/5/
	#url(r'^(?P<question_id>[0-9]+)/$',views.detail,name='detail'),
	# ex: /Mothers_Day/5/results/
	#url(r'^(?P<question_id>[0-9]+)/results/$',views.results,name='results'),
	# ex: /Mothers_Day/5/vote/
	#url(r'^(?P<question_id>[0-9]+)/vote/$',views.vote,name='vote'),
	
