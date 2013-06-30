from django import template
from django.template.defaultfilters import slugify

register = template.Library()

@register.inclusion_tag('main/_breadcrumb.html', takes_context = True)
def breadcrumb_url_2(context, url, id, name):
    return {'name': name, 'url': url + str(id) + '/' + slugify(name)}

@register.inclusion_tag('main/_breadcrumb.html', takes_context = True)
def breadcrumb_url(context, url, name):
    return {'name': name, 'url': url}

@register.inclusion_tag('main/_breadcrumb.html', takes_context = True)
def breadcrumb(context, name):
    return {'name': name}
