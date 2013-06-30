from django import template
from django.template.defaultfilters import slugify

register = template.Library()

@register.inclusion_tag('main/_project.html', takes_context = True)
def project(context, project):
    return {'project': project, 'url': '/projet/' + str(project.id) + '/' + slugify(project.name)}

@register.inclusion_tag('main/_project.html', takes_context = True)
def project_from_skill(context, project, skill):
    return {'project': project, 'skill': skill, 'url': '/competence/' + str(skill.id) + '/' + slugify(skill.name) + '/' + str(project.id) + '/' + slugify(project.name)}

@register.inclusion_tag('main/_project.html', takes_context = True)
def project_from_tag(context, project, tag):
    return {'project': project, 'tag': tag, 'url': '/tag/' + str(tag.id) + '/' + slugify(tag.name) + '/' + str(project.id) + '/' + slugify(project.name)}
