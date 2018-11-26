# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.http import HttpResponse
from shop.views.auth import PasswordResetConfirm
from cms.sitemaps import CMSSitemap
from myshop.sitemap import ProductSitemap
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import  url
from django.core.urlresolvers import reverse
from django.conf.urls import url
from rest_framework import views
from rest_framework import routers
from rest_framework.routers import DefaultRouter


from profile.views import ProfileFormView,ProfileFormAjaxView
from contacts.views import ContactFormView, ContactFormAjaxView,ContactDisplay
from Blogging.views import BlogFormAjaxView,BlogFormView
from shop.views.blogview import BlogList,BlogRetrieveView
from shop.views.jobprofile import jobindex,jobupdateDetails
#from shop.views.profileview import ProfileList,ProfileRetrieveView
from shop.views.profileview import index,updateDetails
from shop.views.commentview import CommentRetrieveView,CommentList



sitemaps = {'cmspages': CMSSitemap,
            'products': ProductSitemap}



def render_robots(request):
    permission = 'noindex' in settings.ROBOTS_META_TAGS and 'Disallow' or 'Allow'
    return HttpResponse('User-Agent: *\n%s: /\n' % permission, content_type='text/plain')

i18n_urls = (
    url(r'^accounts/', include('allauth.urls')),
    url(r'^admin/', include(admin.site.urls)),


    url(r'^password-reset-confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/?$',
        PasswordResetConfirm.as_view(template_name='myshop/pages/password-reset-confirm.html'),
        name='password_reset_confirm'),
    url(r'^', include('cms.urls')),
)
urlpatterns = [
    url(r'^robots\.txt$', render_robots),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    url(r'^shop/', include('shop.urls', namespace='shop')),
    url(r'^multi_form/$', ContactFormAjaxView.as_view(), name='multi_form'),
    url(r'^$', ContactFormView.as_view(), name='contact_form'),
    url(r'^blogging_form/$',BlogFormAjaxView.as_view(),name='blogging_form' ),
    url(r'^$', ProfileFormView.as_view(), name='Profile_Form'),
    url(r'^blogging_form/$',ProfileFormAjaxView.as_view(),name='Profile_form' ),
    url(r'^$', BlogFormView.as_view(), name='Blog_Form'),
    url(r'^contacts/$', CommentList.as_view()),
    url(r'^contacts/(?P<pk>[0-9]+)$', CommentRetrieveView.as_view()),
    url(r'^blogging/$',BlogList.as_view()),
    url(r'^blogging/(?P<pk>[0-9]+)$', BlogRetrieveView.as_view()),
    url(r'^profilelist/$',index,name='profilelist'),
    url(r'^profile/(?P<pk>[0-9]+)$', updateDetails,name='profile_with_pk'),
    url(r'^joblist/$',jobindex,name='joblist'),
    url(r'^job/(?P<pk>[0-9]+)$', jobupdateDetails,name='job_with_pk'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.USE_I18N:
    urlpatterns.extend(i18n_patterns(*i18n_urls))
else:
    urlpatterns.extend(i18n_urls)
urlpatterns.extend(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
