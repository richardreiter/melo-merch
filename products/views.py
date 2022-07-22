from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# object to generate search query
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category
from .forms import ProductForm

# Create your views here.
"""
Many thanks to Chris Zielinski and CI's 'Boutique Ado'
Walkthrough project - a great reference, inspiration and example:
https://github.com/Code-Institute-Solutions/boutique_ado_v1
"""


def all_products(request):
    """
    View to show all products,
    including sorting and search queries
    """

    # return products from db
    products = Product.objects.all()
    # to avoid error when loading products page without search
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            # split into a list at the commas
            categories = request.GET['category'].split(',')
            # use list to filter current query set
            # of all products to only whose category
            # name is in the list
            products = products.filter(category__name__in=categories)
            # filter category down to the ones
            # whose name is in the list from url
            categories = Category.objects.filter(name__in=categories)

        # if text input q
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request,
                    "You didn't enter any search criteria!"
                    )
                return redirect(reverse('products'))
            # case insensitive and name or description
            queries = Q(name__icontains=query) | \
                Q(description__icontains=query)
            # filter method to filter products
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    # products to be available in template
    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """
    View to show individual product details
    """
    # take product id as a param
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }
    # return template including product
    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """
    View to add a product to the shop
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only shop owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to add product. Please ensure the form is valid.'
                )
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """
    Edit a product in the shop
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only shop owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to update product. \
                    Please ensure the form is valid.'
                    )
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """
    Delete a product from the shop
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only shop owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
