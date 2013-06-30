from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from apps.main.models import Skill, Timeline, Project, Tag, VTag
import json
import sys


            # queryset=Skill.objects.order_by('name').order_by('order'),
            # template_name='main/skill_list.html'),

def skill_list(request):

	promoted = list()
	sub = list()

	for s in Skill.objects.order_by('name').order_by('order'):
		if s.sub: sub.append(s)
		else: promoted.append(s)

	return render_to_response('main/skill_list.html', {
		'promoted': promoted,
		'sub': sub
	})


def project_detail(request, project_id):
    p = get_object_or_404(Project, pk = project_id)

    return render_to_response('main/project_detail.html', {
            'project': p
            })

def project_from_skill(request, skill_id, project_id):
    p = get_object_or_404(Project, pk = project_id)
    s = get_object_or_404(Skill, pk = skill_id)

    return render_to_response('main/project_detail.html', {
			'skill': s,
            'project': p
            })

def project_from_tag(request, tag_id, project_id):
    p = get_object_or_404(Project, pk = project_id)
    t = get_object_or_404(Tag, pk = tag_id)

    return render_to_response('main/project_detail.html', {
			'tag': t,
            'project': p
            })

def skill_detail(request, skill_id):

    skill = get_object_or_404(Skill, pk = skill_id)

    return render_to_response('main/skill_detail.html', {
            'skill': skill,
            'projects': skill.project.all().order_by('name')
            })


def tag_detail(request, tag_id):

	return render_to_response('main/tag_detail.html', {
		'tag': Tag.objects.filter(id = tag_id)[0],
		'object_list': Project.objects.filter(tag__id__exact = tag_id).order_by('name')
	})


def skill_detail_tag(request, skill_id, tag_id):

    skill = get_object_or_404(Skill, pk = skill_id)

    return render_to_response('main/skill_detail.html', {
            'skill': skill,
            'projects': skill.project.all(),
            })


def timeline(request):

    dates = list()
    for item in Timeline.objects.all():
        path = ''
        if item.media_file: path = item.media_file.path.url
        elif item.media_path: path = item.media_path

        dates.append({
                'headline': item.headline,
                'text': item.text,
                'startDate': item.startDate.strftime('%y,%m,%d'),
                'endDate': item.endDate and item.endDate.strftime('%y,%m,%d') or False,
                'asset': {'media': path, 'credit': '', 'caption': ''}
                })

    return HttpResponse(json.dumps({
                'timeline':
                    {
                    'headline':'Parcours',
                    'type':'default',
                    'text':'',
                    'startDate':'2007,1,1',
                    'date': dates
                    }
                }), mimetype="application/json")
