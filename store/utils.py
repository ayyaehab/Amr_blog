import json
from .models import *


def cookieCart(request):
    # Create empty cart for now for non-logged in user
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}
        print('CART:', cart)

    items = []
    order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
    cartItems = order['get_cart_items']

    for i in cart:
        # We use try block to prevent items in cart that may have been removed from causing error
        try:
            if (cart[i]['quantity'] > 0):  # items with negative quantity = lot of freebies
                cartItems += cart[i]['quantity']

                product = Product.objects.get(id=i)
                total = (product.price * cart[i]['quantity'])

                order['get_cart_total'] += total
                order['get_cart_items'] += cart[i]['quantity']

                item = {
                    'id': product.id,
                    'product': product,
                    'quantity': cart[i]['quantity'],
                    'get_total': total,
                }
                items.append(item)

            # if product.digital == False:
            # 	order['shipping'] = True
        except:
            pass

    return {'cartItems': cartItems, 'order': order, 'items': items}


def cartData(request):
    cookieData = cookieCart(request)
    cartItems = cookieData['cartItems']
    order = cookieData['order']
    items = cookieData['items']
    return {'cartItems': cartItems, 'order': order, 'items': items}

def guestOrder(request, data, transaction_id):
    fullname = data['shipping']['fullname']
    address = data['shipping']['address']
    phone = data['shipping']['phone']
    whatsapp = data['shipping']['whatsapp']
    city = data['shipping']['city']
    notes = data['shipping']['notes']
    total = data['shipping']['total']
    shipping_cost = data['shipping']['shipping_cost']
    cookieData = cookieCart(request)
    items = cookieData['items']

    customer, created = CheckOut.objects.get_or_create(
            transaction_id= transaction_id,
            fullname=fullname,
            address=address,
            phone=phone,
            whatsapp=whatsapp,
            city=city,
            notes=notes,
            shipping_cost=total,
            products_cost=shipping_cost,
            complete=False,
            )
    for item in items:
        product = Product.objects.get(id=item['id'])
        orderItem = OrderItem.objects.create(
            product=product,
            checkout=customer,
            quantity=(item['quantity'] if item['quantity']>0 else -1*item['quantity']), # negative quantity = freebies
        )
    return customer, orderItem
