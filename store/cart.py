from .models import Book


class Cart:

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')

        if not cart:
            cart = self.session['cart'] = {}

        self.cart = cart

    def add(self, book, quantity=1):
        book_id = str(book.id)

        if book_id in self.cart:
            self.cart[book_id]['quantity'] += quantity
        else:
            self.cart[book_id] = {
                'quantity': quantity,
                'price': str(book.price)
            }

        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, book):
        book_id = str(book.id)

        if book_id in self.cart:
            del self.cart[book_id]

        self.save()

    def __iter__(self):
        book_ids = self.cart.keys()
        books = Book.objects.filter(id__in=book_ids)

        cart = self.cart.copy()

        for book in books:
            cart[str(book.id)]['book'] = book

        for item in cart.values():
            item['price'] = float(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(
            item['quantity']
            for item in self.cart.values()
        )

    def get_total_price(self):
        return sum(
            float(item['price']) * item['quantity']
            for item in self.cart.values()
        )

    def clear(self):
        del self.session['cart']
        self.save()