from django.conf import settings
from django.db import models
from categories.models import Category


class Listing(models.Model):

    LISTING_TYPE_CHOICES = [
        ("SALE", "Sale"),
        ("RENT", "Rent"),
    ]

    agent = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="listings",
    )

    title = models.CharField(max_length=255)

    description = models.TextField()

    price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
    )

    listing_type = models.CharField(
        max_length=10,
        choices=LISTING_TYPE_CHOICES,
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="listings",
    )

    bedrooms = models.PositiveIntegerField()

    bathrooms = models.PositiveIntegerField()

    address = models.CharField(max_length=255)

    city = models.CharField(max_length=100)

    state = models.CharField(max_length=100)

    is_available = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title