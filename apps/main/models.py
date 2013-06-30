from django.db import models
from django.conf import settings

class File(models.Model):
    name = models.CharField(max_length = 32)
    path = models.FileField(upload_to="uploads/")

    def __unicode__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length = 42)

    def __unicode__(self):
        return self.name

# select T.id, T.name, count(PT.tag_id) as count
# from `main_tag` T
# left join `main_project_tag` PT
 # on T.id = PT.tag_id
# group by T.id
class VTag(models.Model):
	id = models.IntegerField(primary_key = True)
	name = models.CharField(max_length = 42)
	count = models.IntegerField()

	class Meta:
		managed = False
		ordering = ['-count']

	def __unicode__(self):
		return self.name

class Project(models.Model):
    name = models.CharField(max_length = 128)
    desc = models.TextField(null = True, blank = True)
    intro = models.TextField(null = True, blank = True)
    tag = models.ManyToManyField(Tag, null = True, blank = True)
    file = models.ManyToManyField(File, null = True, blank = True)
    illustration = models.ForeignKey(File, null = True, blank = True, related_name = '+')

    def __unicode__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length = 128)
    order = models.IntegerField(unique = True, null = True, blank = True)
    sub = models.BooleanField()
    desc = models.TextField()
    tag = models.ManyToManyField(VTag, null = True, blank = True)
    project = models.ManyToManyField(Project, null = True, blank = True)
    file = models.ForeignKey(File, null = True, blank = True)

    def __unicode__(self):
        return self.name

class Timeline(models.Model):
    headline = models.CharField(max_length = 128)
    text = models.TextField()
    startDate = models.DateField()
    endDate = models.DateField(null=True, blank=True)
    media_path = models.CharField(max_length = 256, null = True, blank = True)
    media_file = models.ForeignKey(File, null = True, blank = True)

    def __unicode__(self):
        return self.headline
