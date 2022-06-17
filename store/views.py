from django.http import JsonResponse
from django.shortcuts import render
import json
from store.models import CheckOut, Product, Category
from .utils import cookieCart, cartData, guestOrder
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import datetime


def store(request):
    if 'q' in request.GET:
        q = request.GET['q']
        products = Product.objects.filter(title__icontains=q)
    else:
        products = Product.objects.all()

    category = Category.objects.all()
    data = cartData(request)
    cartItems = data['cartItems']
    page = request.GET.get('page')
    paginator = Paginator(products, 6)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        page = paginator.num_pages
        products = paginator.page(page)

    context = {
        'products': products,
        'cartItems': cartItems,
        'category': category,
        'paginator': paginator
    }
    return render(request, 'store/index.html', context)


def cart(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/cart.html', context)


def checkout(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    # data = cartData(request)

    # cartItems = data['cartItems']

    # context = {'cartItems': cartItems}
    return render(request, 'store/checkout.html', context)


# ----------------mug--------------
def mugs(request):
    data = cartData(request)
    cartItems = data['cartItems']
    mugs = Product.objects.filter(category__name="mug")
    context = {
        'cartItems': cartItems,
        'mugs': mugs
    }
    return render(request, 'store/mugs.html', context)


# ----------------shirt--------------
def shirts(request):
    data = cartData(request)
    cartItems = data['cartItems']
    shirts = Product.objects.filter(category__name="shirt")
    page = request.GET.get('page')
    paginator = Paginator(shirts, 9)
    try:
        shirts = paginator.page(page)
    except PageNotAnInteger:
        shirts = paginator.page(1)
    except EmptyPage:
        page = paginator.num_pages
        shirts = paginator.page(page)

    context = {
        'cartItems': cartItems,
        'shirts': shirts,
        'paginator': paginator,
    }

    return render(request, 'store/shirts.html', context)


def oneproduct(request, slug):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    product = Product.objects.get(slug=slug)

    context = {
        'product': product,
        'items': items,
        'order': order,
        'cartItems': cartItems
    }
    return render(request, 'store/one_product.html', context)


# ----------------book--------------
def books(request):
    data = cartData(request)
    cartItems = data['cartItems']
    books = Product.objects.filter(category__name="book")
    page = request.GET.get('page')
    paginator = Paginator(books, 12)
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        page = paginator.num_pages
        books = paginator.page(page)

    context = {
        'cartItems': cartItems,
        'books': books,
        'paginator': paginator,
    }

    return render(request, 'store/books.html', context)


# ----------------laptop--------------
def laptops(request):
    data = cartData(request)
    cartItems = data['cartItems']
    laptops = Product.objects.filter(category__name="laptop")
    page = request.GET.get('page')
    paginator = Paginator(laptops, 12)
    try:
        laptops = paginator.page(page)
    except PageNotAnInteger:
        laptops = paginator.page(1)
    except EmptyPage:
        page = paginator.num_pages
        laptops = paginator.page(page)

    context = {
        'cartItems': cartItems,
        'laptops': laptops,
        'paginator': paginator,
    }

    return render(request, 'store/laptops.html', context)


# ----------------pc--------------
def pcs(request):
    data = cartData(request)
    cartItems = data['cartItems']
    pcs = Product.objects.filter(category__name="pc")
    page = request.GET.get('page')
    paginator = Paginator(pcs, 12)
    try:
        pcs = paginator.page(page)
    except PageNotAnInteger:
        pcs = paginator.page(1)
    except EmptyPage:
        page = paginator.num_pages
        pcs = paginator.page(page)

    context = {
        'cartItems': cartItems,
        'pcs': pcs,
        'paginator': paginator,
    }

    return render(request, 'store/pcs.html', context)


def accessories(request):
    data = cartData(request)
    cartItems = data['cartItems']
    accessories = Product.objects.filter(category__name="accessories")
    page = request.GET.get('page')
    paginator = Paginator(accessories, 12)
    try:
        accessories = paginator.page(page)
    except PageNotAnInteger:
        accessories = paginator.page(1)
    except EmptyPage:
        page = paginator.num_pages
        accessories = paginator.page(page)

    context = {
        'cartItems': cartItems,
        'accessories': accessories,
        'paginator': paginator,
    }

    return render(request, 'store/accessories.html', context)


def offers(request):
    data = cartData(request)
    cartItems = data['cartItems']
    offers = Product.objects.filter(category__name="offers")
    page = request.GET.get('page')
    paginator = Paginator(offers, 12)
    try:
        offers = paginator.page(page)
    except PageNotAnInteger:
        offers = paginator.page(1)
    except EmptyPage:
        page = paginator.num_pages
        offers = paginator.page(page)

    context = {
        'cartItems': cartItems,
        'offers': offers,
        'paginator': paginator,
    }

    return render(request, 'store/offers.html', context)


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    customer, order = guestOrder(request, data, transaction_id)
    total = float(data['shipping']['total'])
    if total == customer.get_cart_total:
        customer.complete = True
    customer.save()

    return JsonResponse('Payment submitted..', safe=False)
