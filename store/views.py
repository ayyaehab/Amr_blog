from django.shortcuts import render

from store.models import Book, Tshirt, TshirtImg, Mug, LapTop, Pc, MugImg, PcImg, LapTopImg


# Create your views here.
def index(request):
    books = Book.objects.all()

    context = {
        'books': books
    }
    return render(request, 'store/index.html', context)


def checkout(request):
    return render(request, 'store/checkout.html', {})


def shirts(request):
    shirts = Tshirt.objects.all()
    context = {
        'shirts': shirts
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
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'store/books.html', context)


def onebook(request, slug):
    book = Book.objects.get(slug=slug)
    context = {'book': book}
    return render(request, 'store/onebook.html', context)


def product(request):
    return render(request, 'store/product.html', {})


# def store1(request):
#     return render(request, 'store/store.html', {})


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
    mugs = Mug.objects.all()
    context = {
        'mugs': mugs
    }
    return render(request, 'store/mugs.html', context)


# images=MugImg.objects.filter(mug = mug)
def mug(request, slug):
    mug = Mug.objects.get(slug=slug)
    images = MugImg.objects.filter(mug=mug)
    context = {'mug': mug,
               'images': images}
    return render(request, 'store/mug.html', context)


# labtop
def laptops(request):
    laptops = LapTop.objects.all()
    context = {
        'laptops': laptops
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
    pcs = Pc.objects.all()
    context = {
        'pcs': pcs
    }
    return render(request, 'store/pcs.html', context)


def pc(request, slug):
    pc = Pc.objects.get(slug=slug)
    images = PcImg.objects.filter(pc=pc)
    context = {'pc': pc,
               'images': images}
    return render(request, 'store/pc.html', context)
