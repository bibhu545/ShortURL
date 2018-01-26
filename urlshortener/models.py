from django.db import models
from .utils import create_shortcode


class Url(models.Model):
	url = models.CharField(max_length=150,null=False,blank=False)
	shortcode = models.CharField(max_length=50,blank=True,null=True)
	clicks = models.IntegerField(default=0)
	updated = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True)

	def save(self,*args,**kwargs):
		if self.shortcode is None or self.shortcode == '':
			self.shortcode = create_shortcode(self)
		super(Url,self).save(*args,**kwargs)

	def __str__(self):
		return self.url

	def __unicode__(self):
		return self.shortcode