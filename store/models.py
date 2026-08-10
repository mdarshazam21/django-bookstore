from django.db import models
from django.contrib.auth.models import User
from django.db.models import F
from django.db.models import Sum

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.PositiveBigIntegerField(default=0)
    cover_image = models.ImageField(upload_to="book_covers/", blank=True, null=True)

    def __str__(self):
        return self.title


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Order #{self.id}"

    def get_total_cost(self):
        result = self.items.aggregate(total=Sum(F("price") * F("quantity")))
        return result["total"] or 0


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def get_cost(self):
        return self.price * self.quantity

    def __str__(self):
        return f"{self.quantity} x {self.book.title}"
