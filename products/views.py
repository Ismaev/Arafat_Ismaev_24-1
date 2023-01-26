
from django.shortcuts import render
from products.models import Product, Review, Category
# Create your views here.


def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')

def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()

        context = {
            'products': products
        }

        return render(request, 'products/products.html', context=context)


def product_detail_view(request, id):
    if request.method == 'GET':
        product = Product.objects.get(id=id)
        reviews = Review.objects.filter(product=product.obj)

        context = {
            'product': product,
            'comment': reviews
        }

        return render(request, 'products/categories.html', context=context)

def categories(request, id):
    if request.method == 'GET':
        product = Product.objects.all()
        reviews = Review.objects.filter(product=product.obj)
        categories = Category.objects.filter(product=product.obj)

        context = {
            'product': product,
            'description': reviews,
            'category': categories
        }
        return render(request, )
