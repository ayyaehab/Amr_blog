from django.urls import path
from . import views

urlpatterns = [
     path('', views.store, name="store"),
     path('cart', views.cart, name='cart'),
     path('checkout', views.checkout, name='checkout'),

     path('remugs', views.mugs, name='mugs'),
     # path('mug-<slug:slug>',views.mug,name="mug"),

     path('reshirts', views.shirts, name='shirts'),
     # path('shirt-<slug:slug>',views.shirt,name='shirt'),
     path('oneproduct-<slug:slug>',views.oneproduct,name='oneproduct'),

     path('repcs', views.pcs, name='pcs'),
     # path('pc-<slug:slug>', views.pc, name='pc'),

     path('rebooks', views.books, name='books'),
     # path('book-<slug:slug>',views.onebook,name='bookcontent'),

     path('relaptops', views.laptops , name='laptops'),
     # path('laptop-<slug:slug>', views.onelaptop, name='onelaptop'),

     path('accessories', views.accessories, name='accessories'),
     path('offers', views.offers, name='offers'),
     # path('offers-<slug:slug>', views.onelaptop, name='offers'),
     # path('accessore-<slug:slug>', views.onelaptop, name='accessore'),

     path('processorder', views.processOrder, name='processorder'),
     path('productCondition', views.productCondition, name='productCondition'),
    # path('blank', views.blank , name='blank'),
    
    
     
    
    
    
    # path('product', views.product , name='product'),
    # path('store1', views.store1 , name='store1'),
    # for testing
    # path('test', views.test , name='test'),
]
