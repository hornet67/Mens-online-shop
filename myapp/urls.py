from django.urls import path
from . import views

from  django.conf import  settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name='home'),
    path('formal/',views.formal_shirt, name ='formal'),
    path('cart/',views.cart, name='cart'),
    path('checkout/',views.checkout, name='checkout')
]

urlpatterns += static(settings.STATIC_URL,document_root =  settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)