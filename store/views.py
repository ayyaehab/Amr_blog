from django.shortcuts import render

from store.models import Book, Tshirt, TshirtImg, Mug, LapTop, Pc, MugImg, PcImg, LapTopImg
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def index(request):
    books = Book.objects.all()
    mugs = Mug.objects.all()
    pcs = Pc.objects.all()
    laptops = LapTop.objects.all()
    shirts = Tshirt.objects.all()
    page = request.GET.get('page')
    all = [books,mugs,pcs,laptops,shirts]
    paginator = Paginator(all, 1)
    # paginator1 = Paginator(books, 1)
    # paginator2 = Paginator(mugs, 1)
    # paginator3 = Paginator(pcs, 1)
    # paginator4 = Paginator(laptops, 1)
    try:
        all = paginator.page(page)
        # books = paginator1.page(page)
        # mugs = paginator2.page(page)
        # pcs = paginator3.page(page)
        # laptops = paginator4.page(page)
    except PageNotAnInteger:
        all = paginator.page(1)
        # books = paginator1.page(1)
        # mugs = paginator2.page(1)
        # pcs = paginator3.page(1)
        # laptops = paginator4.page(1)
    except EmptyPage:
        page = paginator.num_pages
        # page1 = paginator1.num_pages
        # page2 = paginator2.num_pages
        # page3 = paginator3.num_pages
        # page4 = paginator4.num_pages
        all = paginator.page(page)
        # books = paginator1.page(page1)
        # mugs = paginator2.page(page2)
        # pcs = paginator3.page(page3)
        # laptops = paginator4.page(page4)
    context = {
        'all':all,
        'books': books,
        'paginator': paginator,
        'mugs': mugs,
        'pcs': pcs,
        'laptops': laptops,
        'shirts': shirts,
    }
    return render(request, 'store/index.html', context)


def checkout(request):
    return render(request, 'store/checkout.html', {})


def shirts(request):
    shirts = Tshirt.objects.all().order_by('id')
    page = request.GET.get('page')
    paginator = Paginator(shirts, 1)
    try:
        shirts = paginator.page(page)
    except PageNotAnInteger:
        shirts = paginator.page(1)
    except EmptyPage:
        page = paginator.num_pages
        shirts = paginator.page(page)

    context = {
        'shirts': shirts,
        'paginator': paginator,
    }
    return render(request, 'store/shirts.html', context)


def shirt(request, slug):
    tshirt = Tshirt.objects.get(slug=slug)
    images = TshirtImg.objects.filter(tshirt=tshirt)
    context = {'shirt': tshirt,
               'images': images
               }
    return render(request, 'store/shirt.html', context)


def books(request):
    books = Book.objects.all().order_by('id')
    page = request.GET.get('page')
    paginator = Paginator(books, 3)

    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        page = paginator.num_pages
        books = paginator.page(page)

    context = {
        'books': books,
        'paginator': paginator,
    }
    return render(request, 'store/books.html', context)


def onebook(request, slug):
    book = Book.objects.get(slug=slug)
    context = {'book': book}
    return render(request, 'store/onebook.html', context)


def product(request):
    return render(request, 'store/product.html', {})


def blank(request):
    return render(request, 'store/blank.html', {})


# for testing.
def test(request):
    queryset = Book.objects.all()
    context = {
        'book': queryset
    }
    return render(request, 'store/test.html', context)


def mugs(request):
    mugs = Mug.objects.all().order_by('id')
    page = request.GET.get('page')
    paginator = Paginator(mugs, 3)

    try:
        mugs = paginator.page(page)
    except PageNotAnInteger:
        mugs = paginator.page(1)
    except EmptyPage:
        page = paginator.num_pages
        mugs = paginator.page(page)

    context = {
        'mugs': mugs,
        'paginator': paginator,
    }
    return render(request, 'store/mugs.html', context)


# images=MugImg.objects.filter(mug = mug)
def mug(request, slug):
    mug = Mug.objects.get(slug=slug)

    images = MugImg.objects.filter(mug=mug)

    context = {
        'mug': mug,
        'images': images,
    }
    return render(request, 'store/mug.html', context)


# labtop
def laptops(request):
    laptops = LapTop.objects.all().order_by('id')
    page = request.GET.get('page')
    paginator = Paginator(laptops, 1)

    try:
        laptops = paginator.page(page)
    except PageNotAnInteger:
        laptops = paginator.page(1)
    except EmptyPage:
        page = paginator.num_pages
        laptops = paginator.page(page)

    context = {
        'laptops': laptops,
        'paginator': paginator,
    }
    return render(request, 'store/laptops.html', context)


def onelaptop(request, slug):
    lapTop = LapTop.objects.get(slug=slug)
    images = LapTopImg.objects.filter(lapTop=lapTop)
    context = {'laptop': lapTop,
               'images': images}
    return render(request, 'store/onelaptop.html', context)


# pcs
def pcs(request):
    pcs = Pc.objects.all().order_by('id')
    page = request.GET.get('page')
    paginator = Paginator(pcs, 1)
    try:
        pcs = paginator.page(page)
    except PageNotAnInteger:
        pcs = paginator.page(1)
    except EmptyPage:
        page = paginator.num_pages
        pcs = paginator.page(page)

    context = {
        'pcs': pcs,
        'paginator': paginator,
    }
    return render(request, 'store/pcs.html', context)


def pc(request, slug):
    pc = Pc.objects.get(slug=slug)
    images = PcImg.objects.filter(pc=pc)
    context = {'pc': pc,
               'images': images}
    return render(request, 'store/pc.html', context)
