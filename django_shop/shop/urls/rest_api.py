# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url, include
from rest_framework import routers
#from shop.views.blogview import add_blog

from shop.forms.checkout import ShippingAddressForm, BillingAddressForm
from shop.views.address import AddressEditView
from shop.views.cart import CartViewSet, WatchViewSet
from shop.views.checkout import CheckoutViewSet
from shop.views.catalog import ProductSelectView
from django.conf.urls import  url
from django.core.urlresolvers import reverse



#from shop.views.blogview import BlogFormView, BlogFormAjaxView

router = routers.DefaultRouter()  # TODO: try with trailing_slash=False
router.register(r'cart', CartViewSet, base_name='cart')
router.register(r'watch', WatchViewSet, base_name='watch')
router.register(r'checkout', CheckoutViewSet, base_name='checkout')

urlpatterns = [
    url(r'^select_product/?$',
        ProductSelectView.as_view(),
        name='select-product'),
 #   url(r'^multi_form/$', BlogFormAjaxView.as_view(), name='multi_form'),
  #  url(r'^$', BlogFormView.as_view(), name='Blog_form'),
   # url(r'^my-blog/create-blog/$',add_blog,name='add_blog'),
    url(r'^shipping_address/(?P<priority>({{\s*\w+\s*}}|\d+|add))$',
        AddressEditView.as_view(form_class=ShippingAddressForm),
        name='edit-shipping-address'),
    url(r'^billing_address/(?P<priority>({{\s*\w+\s*}}|\d+|add))$',
        AddressEditView.as_view(form_class=BillingAddressForm),
        name='edit-billing-address'),
    url(r'^', include(router.urls)),


]





