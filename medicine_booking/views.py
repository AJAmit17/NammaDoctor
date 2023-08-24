from django.shortcuts import render, redirect
from .models import Medicine
from .forms import CartForm
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Medicine, Order, OrderItem

def medicine_list(request):
    all_medicines = Medicine.objects.all()
    paginator = Paginator(all_medicines, 9)  # Display 9 medicines per page
    page_number = request.GET.get('page')
    medicines = paginator.get_page(page_number)
    
    cart = request.session.get('cart', {})
    form = CartForm(request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            medicine_id = request.POST.get('medicine_id')
            quantity = form.cleaned_data['quantity']
            cart[medicine_id] = cart.get(medicine_id, 0) + quantity
            request.session['cart'] = cart
            return redirect('view_cart')
    
    return render(request, 'medicine_booking/medicine_list.html', {'medicines': medicines, 'form': form})

def medicine_detail(request, medicine_id):
    medicine = Medicine.objects.get(pk=medicine_id)
    form = CartForm(request.POST or None)
    
    if form.is_valid():
        quantity = form.cleaned_data['quantity']
        cart = request.session.get('cart', {})
        cart[medicine_id] = cart.get(medicine_id, 0) + quantity
        request.session['cart'] = cart
        return redirect('view_cart')
    
    return render(request, 'medicine_booking/medicine_detail.html', {'medicine': medicine, 'form': form})

def view_cart(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total_price = 0
    for medicine_id, quantity in cart.items():
        medicine = Medicine.objects.get(pk=medicine_id)
        total_price += medicine.price * quantity
        cart_items.append({'medicine': medicine, 'quantity': quantity})
    return render(request, 'medicine_booking/cart.html', {'cart_items': cart_items, 'total_price': total_price})

def place_order(request):
    order = Order.objects.create(user=request.user)  # Create a new order instance
    cart = request.session.get('cart', {})
    ordered_items = []  # Initialize a list to store ordered items
    total_price = 0
    
    for medicine_id, quantity in cart.items():
        medicine = Medicine.objects.get(pk=medicine_id)
        order_item = OrderItem.objects.create(order=order, medicine=medicine, quantity=quantity)
        ordered_items.append(order_item)  # Add the order item to the list
        total_price += medicine.price * quantity
    
    order.total_price = total_price
    order.save()
    
    request.session['cart'] = {}
    return render(request, 'medicine_booking/order_success.html', {'ordered_items': ordered_items, 'total_price': total_price})


def order_successful(request):
    return render(request, 'medicine_booking/order_success.html')