from django.urls import path
from . import views


urlpatterns = [
    
    path('', views.index , name='index'),
    path('blank', views.blank , name='blank'),
    path('checkout', views.checkout , name='checkout'),
    path('repcs', views.pcs, name='pcs'),
    path('pc-<slug:slug>', views.pc, name='pc'),
    path('relaptops', views.laptops , name='laptops'),
    path('rebooks', views.books, name='books'),
    path('book-<slug:slug>',views.onebook,name='bookcontent'),
    path('laptop-<slug:slug>', views.onelaptop, name='onelaptop'),
    path('reshirts', views.shirts, name='shirts'),
    path('shirt-<slug:slug>',views.shirt,name='shirt'),
    path('remugs', views.mugs, name='mugs'),
    path('mug-<slug:slug>',views.mug,name="mug"),
    path('product', views.product , name='product'),
    # path('store1', views.store1 , name='store1'),
    #for testing 
    path('test', views.test , name='test'),
]
