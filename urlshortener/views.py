from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Url

def redirect_view(request,short_code=None,*args,**kwargs):
	obj = Url.objects.get(shortcode=short_code)
	status = obj.url.startswith('https://')
	obj.clicks += 1
	obj.save()
	if not status:
		return HttpResponseRedirect('http://'+obj.url)
	return HttpResponseRedirect(obj.url)

def homepage(request):
	context = {}
	if request.POST:
		new_url = request.POST.get("url")
		# obj,created = Url.objects.get_or_create(url=new_url)
		status = Url.objects.filter(url=new_url).exists()
		if not status:
			obj = Url.objects.create(url=new_url)
			new_context = {
				"obj":obj
			}
			return render(request,"success.html",new_context)
		if status:
			# Url.objects.get(url='www.google.com')
			obj = Url.objects.get(url=new_url)
			new_context = {
				"obj":obj,
				# "urll":new_url
			}
			return render(request,"already_exists.html",new_context)
	return render(request,"home.html",context)