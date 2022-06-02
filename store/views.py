from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views import View

from store.models import Products, Order, Customer, Category


def Cart(request):
    return render(request, "store/cart.html", {})


class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Products.get_products_by_id(list(cart.keys()))
        print(address, phone, customer, cart, products)

        for product in products:
            print(cart.get(str(product.id)))
            order = Order(customer=Customer(id=customer),
                          product=product,
                          price=product.price,
                          address=address,
                          phone=phone,
                          quantity=cart.get(str(product.id)))
            order.save()
        request.session['cart'] = {}

        return redirect('cart')


class OrderView(View):

    def get(self, request):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        print(orders)
        return render(request, 'cart.html', {'orders': orders})


# Create your views here.
class Index(View):

    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print('cart', request.session['cart'])
        return redirect('homepage')

    def get(self, request):
        # print()
        return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')


def store(request):
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Products.get_all_products_by_categoryid(categoryID)
    else:
        products = Products.get_all_products()

    data = {}
    data['products'] = products
    data['categories'] = categories

    print('you are : ', request.session.get('email'))
    return render(request, 'index.html', data)

# from django.shortcuts import render
#
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#
#
# # Create your views here.
# def index(request):
#     books = Book.objects.all()
#     mugs = Mug.objects.all()
#     pcs = Pc.objects.all()
#     laptops = LapTop.objects.all()
#     shirts = Tshirt.objects.all()
#     page = request.GET.get('page')
#     paginator0 =Paginator(shirts, 1)
#     paginator1 = Paginator(books, 1)
#     paginator2 = Paginator(mugs, 1)
#     paginator3 = Paginator(pcs, 1)
#     paginator4 = Paginator(laptops, 1)
#     try:
#         shirts = paginator0.page(page)
#         books = paginator1.page(page)
#         mugs = paginator2.page(page)
#         pcs = paginator3.page(page)
#         laptops = paginator4.page(page)
#     except PageNotAnInteger:
#         shirts = paginator0.page(1)
#         books = paginator1.page(1)
#         mugs = paginator2.page(1)
#         pcs = paginator3.page(1)
#         laptops = paginator4.page(1)
#     except EmptyPage:
#         page = paginator0.num_pages
#         page1 = paginator1.num_pages
#         page2 = paginator2.num_pages
#         page3 = paginator3.num_pages
#         page4 = paginator4.num_pages
#
#         shirts = paginator1.page(page)
#         books = paginator1.page(page1)
#         mugs = paginator2.page(page2)
#         pcs = paginator3.page(page3)
#         laptops = paginator4.page(page4)
#     context = {
#         'books': books,
#         'paginator': paginator0,
#         'paginator1': paginator1,
#         'paginator2': paginator2,
#         'paginator3': paginator3,
#         'paginator4': paginator4,
#         'mugs': mugs,
#         'pcs': pcs,
#         'laptops': laptops,
#         'shirts': shirts,
#     }
#     return render(request, 'store/index.html', context)
#
#
# def checkout(request):
#     return render(request, 'store/checkout.html', {})
#
#
# def shirts(request):
#     shirts = Tshirt.objects.all().order_by('id')
#     page = request.GET.get('page')
#     paginator = Paginator(shirts, 1)
#     try:
#         shirts = paginator.page(page)
#     except PageNotAnInteger:
#         shirts = paginator.page(1)
#     except EmptyPage:
#         page = paginator.num_pages
#         shirts = paginator.page(page)
#
#     context = {
#         'shirts': shirts,
#         'paginator': paginator,
#     }
#     return render(request, 'store/shirts.html', context)
#
#
# def shirt(request, slug):
#     tshirt = Tshirt.objects.get(slug=slug)
#     images = TshirtImg.objects.filter(tshirt=tshirt)
#     context = {'shirt': tshirt,
#                'images': images
#                }
#     return render(request, 'store/shirt.html', context)
#
#
# def books(request):
#     books = Book.objects.all().order_by('id')
#     page = request.GET.get('page')
#     paginator = Paginator(books, 3)
#
#     try:
#         books = paginator.page(page)
#     except PageNotAnInteger:
#         books = paginator.page(1)
#     except EmptyPage:
#         page = paginator.num_pages
#         books = paginator.page(page)
#
#     context = {
#         'books': books,
#         'paginator': paginator,
#     }
#     return render(request, 'store/books.html', context)
#
#
# def onebook(request, slug):
#     book = Book.objects.get(slug=slug)
#     context = {'book': book}
#     return render(request, 'store/onebook.html', context)
#
#
# def product(request):
#     return render(request, 'store/product.html', {})
#
#
# def blank(request):
#     return render(request, 'store/blank.html', {})
#
#
# # for testing.
# def test(request):
#     queryset = Book.objects.all()
#     context = {
#         'book': queryset
#     }
#     return render(request, 'store/test.html', context)
#
#
# def mugs(request):
#     mugs = Mug.objects.all().order_by('id')
#     page = request.GET.get('page')
#     paginator = Paginator(mugs, 3)
#
#     try:
#         mugs = paginator.page(page)
#     except PageNotAnInteger:
#         mugs = paginator.page(1)
#     except EmptyPage:
#         page = paginator.num_pages
#         mugs = paginator.page(page)
#
#     context = {
#         'mugs': mugs,
#         'paginator': paginator,
#     }
#     return render(request, 'store/mugs.html', context)
#
#
# # images=MugImg.objects.filter(mug = mug)
# def mug(request, slug):
#     mug = Mug.objects.get(slug=slug)
#
#     images = MugImg.objects.filter(mug=mug)
#
#     context = {
#         'mug': mug,
#         'images': images,
#     }
#     return render(request, 'store/mug.html', context)
#
#
# # labtop
# def laptops(request):
#     laptops = LapTop.objects.all().order_by('id')
#     page = request.GET.get('page')
#     paginator = Paginator(laptops, 1)
#
#     try:
#         laptops = paginator.page(page)
#     except PageNotAnInteger:
#         laptops = paginator.page(1)
#     except EmptyPage:
#         page = paginator.num_pages
#         laptops = paginator.page(page)
#
#     context = {
#         'laptops': laptops,
#         'paginator': paginator,
#     }
#     return render(request, 'store/laptops.html', context)
#
#
# def onelaptop(request, slug):
#     lapTop = LapTop.objects.get(slug=slug)
#     images = LapTopImg.objects.filter(lapTop=lapTop)
#     context = {'laptop': lapTop,
#                'images': images}
#     return render(request, 'store/onelaptop.html', context)
#
#
# # pcs
# def pcs(request):
#     pcs = Pc.objects.all().order_by('id')
#     page = request.GET.get('page')
#     paginator = Paginator(pcs, 1)
#     try:
#         pcs = paginator.page(page)
#     except PageNotAnInteger:
#         pcs = paginator.page(1)
#     except EmptyPage:
#         page = paginator.num_pages
#         pcs = paginator.page(page)
#
#     context = {
#         'pcs': pcs,
#         'paginator': paginator,
#     }
#     return render(request, 'store/pcs.html', context)
#
#
# def pc(request, slug):
#     pc = Pc.objects.get(slug=slug)
#     images = PcImg.objects.filter(pc=pc)
#     context = {'pc': pc,
#                'images': images}
#     return render(request, 'store/pc.html', context)
