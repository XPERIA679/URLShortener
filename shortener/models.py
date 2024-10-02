from django.db import models
import string
import random

class URL(models.Model):
    original_url = models.URLField(max_length=2083)
    shortened_url = models.CharField(max_length=10, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.original_url} to {self.shortened_url}"

    def save(self, *args, **kwargs):
        if not self.shortened_url:
            self.shortened_url = self.generate_shortened_url()
        super().save(*args, **kwargs)

    def generate_shortened_url(self):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=6))
