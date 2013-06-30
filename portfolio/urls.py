from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + patterns('',
    # Examples:
    # url(r'^$', 'portfolio.views.home', name='home'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^formation/$', TemplateView.as_view(template_name="main/school.html"), name="school"),
    url(r'^parcours/$', TemplateView.as_view(template_name="main/career.html"), name="career"),
    url(r'^profile/$', TemplateView.as_view(template_name="main/profil.html"), name="profil"),

    url(r'^$', TemplateView.as_view(template_name="main/profil.html"), name="profil"),
    #url(r'^$', direct_to_template,
    #    {'template': 'main/profil.html', 'extra_context': { 'index': True } },
    #    name = 'index'),

    url(r'^', include('apps.main.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
)
