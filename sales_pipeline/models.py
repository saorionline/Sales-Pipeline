from django.db import models

# Create your models here.
from django.db import models

class Transaction(models.Model):
    # Defining the type of movement
    TRANSACTION_TYPES = [
        ('IN', 'Income'),
        ('EX', 'Expense'),
    ]

    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=2, choices=TRANSACTION_TYPES)
    date_created = models.DateTimeField(auto_now_add=True)
    
    # This helps identify the source if it comes from an API later
    source_id = models.CharField(max_length=100, unique=True, blank=True, null=True)

    def __str__(self):
        return f"{self.description} - ${self.amount}"