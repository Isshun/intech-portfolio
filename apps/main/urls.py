from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView, TemplateView
from apps.main.models import Skill, VTag

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # url(r'competence/$',
        # ListView.as_view(
            # queryset=Skill.objects.order_by('name').order_by('order'),
            # template_name='main/skill_list.html'),
        # name='skill_index'),
    url(r'^timeline/$', 'apps.main.views.timeline', name='timeline'),
	
	# Tag
    url(r'^tag/(?P<tag_id>\d+)/(.*)/(?P<project_id>\d+)/(.*)/$', 'apps.main.views.project_from_tag', name='project_from_tag'),
    url(r'^tag/(?P<tag_id>\d+)/(.*)/$', 'apps.main.views.tag_detail', name='tag_detail'),
    url(r'^tag/$', ListView.as_view(model=VTag, template_name='main/tag_list.html'), name='tag_list'),

	# Project
    url(r'^project/(?P<project_id>\d+)/(.*)/$', 'apps.main.views.project_detail', name='project_detail'),

	# Skill
    url(r'^competence/$', 'apps.main.views.skill_list', name='skill_index'),
    url(r'^competence/(?P<skill_id>\d+)/(.*)/(?P<project_id>\d+)/(.*)/$', 'apps.main.views.project_from_skill', name='project_from_skill'),
    url(r'^competence/(?P<skill_id>\d+)/tag/(?P<tag_id>\d+)/$', 'apps.main.views.skill_detail_tag', name='skill_detail_tag'),
    url(r'^competence/(?P<skill_id>\d+)/(.*)/$', 'apps.main.views.skill_detail', name='skill_detail'),
)
