"""ecom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView, RedirectView
from django.contrib.auth.views import LogoutView

# from products.views import (
#         ProductListView,
#         product_list_view,
#         ProductDetailView,
#         ProductDetailSlugView,
#         product_detail_view,
#         ProductFeaturedListView,
#         ProductFeaturedDetailView,
#         )
from addresses.views import checkout_address_create_view, checkout_address_reuse_view
from .views import home_page, about_page, cultura_page, comunidad_page, seguimiento_page, cambios_page, ayuda_page
from .views import contact_page
from billing.views import payment_method_view, payment_method_createview
from carts.views import cart_detail_api_view
from accounts.views import LoginView, RegisterView, guest_register_view

urlpatterns = [
    url(r'^$', home_page, name='home' ),
    url(r'^about/$', about_page, name='about' ),
    url(r'^cultura/$', cultura_page, name='cultura' ),
    url(r'^comunidad/$', comunidad_page, name='comunidad' ),
    url(r'^seguimiento/$', seguimiento_page, name='seguimiento' ),
    url(r'^cambios/$', cambios_page, name='cambios' ),
    url(r'^ayuda/$', ayuda_page, name='ayuda' ),
    # url(r'^accounts/login/$', RedirectView.as_view(url='/login')),
    # url(r'^accounts/', include(("accounts.urls",'cart'), namespace='accounts')),
    url(r'^contact/$', contact_page, name='contact' ),
    url(r'^cart/', include(("carts.urls",'cart'), namespace='cart')),
    url(r'^checkout/address/create/$', checkout_address_create_view, name='checkout_address_create'),
    url(r'^checkout/address/reuse/$', checkout_address_reuse_view, name='checkout_address_reuse'),
    url(r'^register/guest/$', guest_register_view, name='guest_register' ),
    url(r'^login/$', LoginView.as_view(), name='login' ),
    url(r'^api/cart/$', cart_detail_api_view, name='api-cart' ),
    url(r'^logout/$', LogoutView.as_view(), name='logout' ),
    url(r'^billing/payment-method/$', payment_method_view, name='billing-payment-method'),
    url(r'^billing/payment-method/create/$', payment_method_createview, name='billing-payment-method-endpoint'),
    url(r'^register/$', RegisterView.as_view(), name='register' ),
    url(r'^bootstrap/$', TemplateView.as_view(template_name='bootstrap/example.html') ),
    url(r'^products/', include(("products.urls",'products'), namespace='products')),
    url(r'^search/', include(("search.urls",'search'), namespace='search')),
    # url(r'^featured/$', ProductFeaturedListView.as_view() ),
    # url(r'^featured/(?P<pk>\d+)/$', ProductFeaturedDetailView.as_view() ),
    # url(r'^products/$', ProductListView.as_view() ),
    # url(r'^products-fbv/$', product_list_view ),
    # # url(r'^products/(?P<pk>\d+)/$', ProductDetailView.as_view() ),
    # url(r'^products/(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view() ),
    # url(r'^products-fbv/(?P<pk>\d+)/$', product_detail_view ),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns =urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns =urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
