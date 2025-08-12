from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Invoice, InvoiceItem, Customer
from .models import Product
from django.db import transaction

def create_invoice(request):
    products = Product.objects.all()
    customers = Customer.objects.all()

    if request.method == "POST":
        customer_id = request.POST.get("customer")
        customer = Customer.objects.get(id=customer_id) if customer_id else None

        invoice = Invoice.objects.create(customer=customer)
        total = 0

        for product in products:
            qty = int(request.POST.get(f"quantity_{product.id}", 0))
            if qty > 0:
                InvoiceItem.objects.create(
                    invoice=invoice,
                    product=product,
                    quantity=qty,
                    price=product.price
                )
                total += product.price * qty
                product.stock -= qty
                product.save()

        invoice.total = total
        invoice.save()

        return redirect('invoice_detail', invoice_id=invoice.id)

    return render(request, 'create_invoice.html', {
        'products': products,
        'customers': customers
    })
