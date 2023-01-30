
from django.shortcuts import render, redirect
from products.models import Product, Review, Category
from products.forms import ProductCreateForm, ReviewCreateForm
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
        product_obj = Product.objects.get(id=id)
        reviews = Review.objects.filter(post=product_obj)

        context = {
            'product': product_obj,
            'review': reviews,
            'form': ReviewCreateForm
        }

        return render(request, 'products/categories.html', context=context)
    if request.method == 'PRODUCT':
        product_obj = Product.objects.get(id=id)
        reviews = Review.objects.filter(product=product_obj)

        form = ReviewCreateForm(data=request.PRODUCT)
        if form.is_valid():
            Review.objects.create(
                product=product_obj,
                text=form.cleaned_data.get('text')
            )
            return redirect(f'/products/{product_obj.id}')
        return render(request, 'products/categories.html', context={
            'product': product_obj,
            'review': reviews,
            'form': form
        })


def categories(request):
    if request.method == 'GET':
        return render(request, 'products/categories.html')

def create_product_view(request):
    if request.method == 'GET':
        context = {
            'form': ProductCreateForm
        }
        return render(request, 'products/create.html', context=context)
    if request.method == 'PRODUCT':
        form = ProductCreateForm(data=request.PRODUCT)
        if form.is_valid():
            Product.objects.create(
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                rate=form.cleaned_data.get('rate' if form.cleaned_data['rate'] is not None else 5)
            )
            return redirect('/posts/')
        return render(request, 'products/create.html', context={
            'form': form
        })