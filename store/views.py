from django.shortcuts import render
import json
from store.models import Product
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
