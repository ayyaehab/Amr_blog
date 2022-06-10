from django.shortcuts import render
import json
from store.models import Product,ProductImg
from .utils import cookieCart, cartData

def store(request):
	data = cartData(request)

	cartItems = data['cartItems']

	products = Product.objects.all()
	context = {'products':products, 'cartItems':cartItems}
	return render(request, 'store/index.html', context)

def cart(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'store/cart.html', context)


def checkout(request):
	data = cartData(request)

	cartItems = data['cartItems']

	
	context = {'cartItems':cartItems}
	return render(request, 'store/checkout.html', context)

# ----------------mug--------------
def mugs(request):
    mugs = Product.objects.filter(category__name="mug")
    context = {
        'mugs': mugs
    }
    return render(request, 'store/mugs.html', context)


def mug(request, slug):
    mug = Product.objects.get(slug=slug)
    images = ProductImg.objects.filter(product=mug)
    context = {'mug': mug,
               'images': images}
    return render(request, 'store/mug.html', context)

# ----------------shirt--------------
def shirts(request):
    shirts = Product.objects.filter(category__name="shirt")
    context = {
        'shirts': shirts
    }
    return render(request, 'store/shirts.html', context)


def shirt(request, slug):
    shirt = Product.objects.get(slug=slug)
    images = ProductImg.objects.filter(product=shirt)
    
    context = {'shirt': shirt,
               'images': images
               }
    return render(request, 'store/shirt.html', context)

# ----------------book--------------
def books(request):
    books = Product.objects.filter(category__name="book")
    context = {
        'books': books
    }
    return render(request, 'store/books.html', context)

def onebook(request, slug):
    book = Product.objects.get(slug=slug)
    images = ProductImg.objects.filter(product=book)
    context = {'book': book,
               'images':images}
    return render(request, 'store/onebook.html', context)
# ----------------laptop--------------
def laptops(request):
    laptops = Product.objects.filter(category__name="laptop")
    context = {
        'laptops': laptops
    }
    return render(request, 'store/laptops.html', context)


def onelaptop(request, slug):
    laptop = Product.objects.get(slug=slug)
    images = ProductImg.objects.filter(product=laptop)
    context = {'laptop': laptop,
               'images': images}
    return render(request, 'store/onelaptop.html', context)
# ----------------pc--------------
def pcs(request):
    pcs = Product.objects.filter(category__name="pc")
    context = {
        'pcs': pcs
    }
    return render(request, 'store/pcs.html', context)


def pc(request, slug):
    pc = Product.objects.get(slug=slug)
    images = ProductImg.objects.filter(product=pc)
    context = {'pc': pc,
               'images': images}
    return render(request, 'store/pc.html', context)

# def cart(request):

# 	#Create empty cart for now for non-logged in user
# 	try: 
# 		cart = json.loads(request.COOKIES['cart'])
        
# 	except:
# 		cart = {}
# 		print('CART:', cart)

# 	items = []
# 	order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
# 	cartItems = order['get_cart_items']

# 	for i in cart:
# 		#We use try block to prevent items in cart that may have been removed from causing error
			
# 			 #items with negative quantity = lot of freebies  
# 				cartItems += cart[i]['quantity']

# 				product = Product.objects.get(id=i)
# 				total = (product.price * cart[i]['quantity'])

# 				order['get_cart_total'] += total
# 				order['get_cart_items'] += cart[i]['quantity']

# 				item = {
#                     'product':product,
#                     'quantity':cart[i]['quantity'],
#                     'get_total':total
# 				}
# 				items.append(item)
                
				
# 	context = {'items':items, 'order':order, 'cartItems':cartItems}		
# 	return render(request, 'store/cart.html', context)

# def checkout(request):
#     return render(request, 'store/checkout.html', {})
