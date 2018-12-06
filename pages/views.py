from django.shortcuts import render,HttpResponse
from pages.models import Post
from django.core import serializers

# Create your views here.
def post_list(request):
    leads_as_json = serializers.serialize('json', Post.objects.all())
    return HttpResponse(leads_as_json, content_type='json')
