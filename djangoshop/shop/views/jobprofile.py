from cms.utils import get_language_from_request
from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.parsers import JSONParser
from jobs.models import Job
from rest_framework import mixins
from rest_framework.views import APIView
from shop.serializers.jobsserializer import JobSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
import os
from rest_framework.reverse import reverse

def jobupdateDetails(request, pk):
    jobs = Job.objects.get(pk=pk)
    return render(request, 'shop/jobsdisplay/jobdetail.html', {'jobs': jobs, 'pk': pk})

def jobindex(request):
    jobs = Job.objects.all()
    job = Job.objects
    return render(request, 'shop/jobsdisplay/joblist.html', {'jobs': jobs, 'job': job})

class ProfileList(generics.GenericAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'shop/Profiles/displayprofile.html'
    model = Job

    def get(self, request):
      queryset = Job.objects.all()
      return Response({'job': queryset})



class ProfileRetrieveView(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):

    queryset = Job.objects.all()
    renderer_classes = (TemplateHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return Response({'profile': self.object}, template_name='shop/Profiles/displayprofile.html')



