from cms.utils import get_language_from_request
from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.parsers import JSONParser
from profile.models import Profile
from rest_framework import mixins
from rest_framework.views import APIView
from shop.serializers.profileserializer import ProfileSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
import os
from rest_framework.reverse import reverse

def updateDetails(request, pk):
    profiles = Profile.objects.get(pk=pk)
    return render(request, 'shop/Profiles/displayprofile.html', {'profiles': profiles, 'pk': pk})

def index(request):
    profiles = Profile.objects.all()
    profile = Profile.objects
    return render(request, 'shop/Profiles/profilelist.html', {'profiles': profiles, 'profile': profile})

class ProfileList(generics.GenericAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'shop/Profiles/displayprofile.html'
    model = Profile

    def get(self, request):
      queryset = Profile.objects.all()
      return Response({'profile': queryset})



class ProfileRetrieveView(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):

    queryset = Profile.objects.all()
    renderer_classes = (TemplateHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return Response({'profile': self.object}, template_name='shop/Profiles/displayprofile.html')



