from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .cart import Cart
from .forms import OrderCreateForm
from .models import OrderItem
from django.contrib.auth.decorators import login_required
from .models import Order

# Create your views here.ur


def book_list(request):
    books = Book.objects.all()
    context = {"books": books}
    return render(request, "store/book_list.html", context)


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    context = {"book": book}
    return render(request, "store/book_detail.html", context)


def cart_add(request, pk):
    cart = Cart(request)
    book = get_object_or_404(Book, pk=pk)
    cart.add(book=book)
    return redirect("cart_detail")


def cart_remove(request, pk):
    cart = Cart(request)
    book = get_object_or_404(Book, pk=pk)
    cart.remove(book)
    return redirect("cart_detail")


def cart_detail(request):
    cart = Cart(request)
    return render(request, "store/cart_detail.html", {"cart": cart})


def order_create(request):
    cart = Cart(request)
    if request.method == "POST":
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if request.user.is_authenticated:
                order.user = request.user
            order.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    book=item["book"],
                    price=item["price"],
                    quantity=item["quantity"],
                )
            cart.clear()
            return render(request, "store/order_created.html", {"order": order})
    else:
        form = OrderCreateForm()
    return render(request, "store/order_create.html", {"cart": cart, "form": form})


@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by("-created_at")
    context = {"orders": orders}
    return render(request, "store/order_history.html", context)
