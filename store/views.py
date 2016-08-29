from django.shortcuts import render, redirect
from django.contrib import messages
from models import Product
import stripe

# Create your views here.


def storefront(request):
    product = Product.objects.all()
    return render(request, 'store_front.html', {'product': product})


def checkout(request):
    return render(request, 'checkout.html')


def charge(request):
    if request.method != 'POST':
        return redirect('store_front.html')

    if 'stripeToken' not in request.POST:
        messages.error(request, 'Uh oh, something went wrong, please try again!')
        return redirect('store_front.html')

    customer = stripe.Customer.create(
        email=request.POST['stripeEmail'],
        source=request.POST['stripeToken'],
    )

    amount = 2000

    stripe.Charge.create(
        customer=customer.id,
        currency="usd",
        amount=amount,
        description='Card Payment 5ify'
    )

    messages.success(request, 'Success')
    return redirect('thanks')


def thanks(request):
    return render(request, 'thank_you.html')