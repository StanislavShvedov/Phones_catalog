from django.shortcuts import render, get_object_or_404

from phones.models import Phone


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort', '')
    if sort == 'name':
        phones = Phone.objects.all().order_by('name')
    elif sort == 'name-reverse':
        phones = Phone.objects.all().order_by('-name')
    elif sort == 'min_price':
        phones = Phone.objects.all().order_by('price')
    elif sort == 'max_price':
        phones = Phone.objects.all().order_by('-price')
    else:
        phones = Phone.objects.all()
    context = {
        'phones': phones
    }
    return render(request, template, context)


def show_product(request, slug):
    phone = get_object_or_404(Phone, slug=slug)
    print(phone)
    template = 'product.html'
    context = {
        'phone': phone
    }
    return render(request, template, context)